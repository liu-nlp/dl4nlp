def read_data(corpus_file):
    with open(corpus_file, encoding='utf-8') as f:
        X = []
        Y = []
        words = []
        labels = []
        for line in f:
            line = line.strip()
            if not line:
                X.append(words)
                Y.append(labels)
                words = []
                labels = []
            else:
                columns = line.split()
                words.append(columns[0])
                labels.append(columns[-1])
        return X, Y
    

from collections import defaultdict, Counter    
import torch
from torch import nn

PAD = '___PAD___'
UNKNOWN = '___UNKNOWN___'
BOS = '___BOS___'
EOS = '___EOS___'

class Vocabulary:
    """Manages the numerical encoding of the vocabulary."""
    
    def __init__(self, max_voc_size=None, include_unknown=True, lower=False,
                 character=False, gensim_model=None):

        self.include_unknown = include_unknown
        self.dummies = [PAD, UNKNOWN, BOS, EOS] if self.include_unknown else [PAD, BOS, EOS]
        
        self.character = character
        
        if not gensim_model:
            # String-to-integer mapping
            self.stoi = None
            # Integer-to-string mapping
            self.itos = None
            # Maximally allowed vocabulary size.
            self.max_voc_size = max_voc_size
            self.lower = lower
            self.vectors = None
        else:
            self.vectors = gensim_model[0]
            self.itos = self.dummies + gensim_model[1]
            self.stoi = {s:i for i, s in enumerate(self.itos)}
            self.lower = not gensim_model[2]
            
    def make_embedding_layer(self, finetune=True, emb_dim=None):
        if self.vectors is not None:
            emb_dim = self.vectors.shape[1]
            emb_layer = nn.Embedding(len(self.itos), emb_dim)

            with torch.no_grad():
                # Copy the pre-trained embedding weights into our embedding layer.
                emb_layer.weight[len(self.dummies):, :] = self.vectors

            #print(f'Emb shape: {emb_layer.weight.shape}, voc size: {len(self.itos)}')
        else:
            emb_layer = nn.Embedding(len(self.itos), emb_dim)
        
        if not finetune:
            # If we don't fine-tune, create a tensor where we don't compute the gradients.
            emb_layer.weight = nn.Parameter(emb_layer.weight, requires_grad=False)
        
        return emb_layer
        
    def build(self, seqs):
        """Builds the vocabulary."""
        
        if self.character:
            seqs = [ [c for w in seq for c in w] for seq in seqs ]
        
        if self.lower:
            seqs = [ [s.lower() for s in seq] for seq in seqs ]
        
        # Sort all words by frequency
        word_freqs = Counter(w for seq in seqs for w in seq)
        word_freqs = sorted(((f, w) for w, f in word_freqs.items()), reverse=True)

        # Build the integer-to-string mapping. The vocabulary starts with the two dummy symbols,
        # and then all words, sorted by frequency. Optionally, limit the vocabulary size.
        
        if self.max_voc_size:
            self.itos = self.dummies + [ w for _, w in word_freqs[:self.max_voc_size-len(dummies)] ]
        else:
            self.itos = self.dummies + [ w for _, w in word_freqs ]

        # Build the string-to-integer map by just inverting the aforementioned map.
        self.stoi = { w: i for i, w in enumerate(self.itos) }
                
    def encode(self, seqs):
        """Encodes a set of documents."""
        unk = self.stoi.get(UNKNOWN)
        bos = self.stoi.get(BOS)
        eos = self.stoi.get(EOS)
        
        if self.character:
            if self.lower:
                seqs = [ [[c for c in w.lower()] for w in seq] for seq in seqs ]
            return [[[bos,eos]]+[[bos]+[self.stoi.get(c, unk) for c in w]+[eos] for w in seq]+[[bos,eos]] for seq in seqs]
        else:
            if self.lower:
                seqs = [ [s.lower() for s in seq] for seq in seqs ]
            return [[bos]+[self.stoi.get(w, unk) for w in seq]+[eos] for seq in seqs]

    def get_unknown_idx(self):
        """Returns the integer index of the special dummy word representing unknown words."""
        return self.stoi[UNKNOWN]
    
    def get_pad_idx(self):
        """Returns the integer index of the special padding dummy word."""
        return self.stoi[PAD]
    
    def __len__(self):
        return len(self.itos)
    
    
    
from torch.utils.data import Dataset, DataLoader
import random
random.seed(0)

class SequenceDataset(Dataset):
    """A Dataset that stores a list of sentences and their corresponding labels."""
    def __init__(self, Xwords, Y, Xchars=None, word_dropout_prob=None, word_dropout_id=None):
        self.Xwords = Xwords
        self.Xchars = Xchars
        self.Y = Y
        self.word_dropout_prob = word_dropout_prob
        self.word_dropout_id = word_dropout_id
        
    def __getitem__(self, idx):
        if self.word_dropout_prob:
            words = [ w if random.random() > self.word_dropout_prob else self.word_dropout_id for w in self.Xwords[idx] ]
        else:
            words = self.Xwords[idx]
        
        if self.Xchars:
            return words, self.Y[idx], self.Xchars[idx]
        else:
            return words, self.Y[idx]
        
    def __len__(self):
        return len(self.Y)

class SequenceBatcher:
    """A collator that builds a batch from a number of sentence--labeling pairs."""
    
    def __init__(self, device):
        self.device = device
    
    def __call__(self, XY):
        """Build a batch from a number of sentences. Returns two tensors X and Y, where
        X is the sentence tensor, of shape [n_sentences, max_sen_length]

        and 
        
        Y is the label tensor, of the same shape as X.
        """
        
        # Assume that the padding id is 0.
        pad_id = 0
                
        # How long is the longest document in this batch?
        max_sen_len = max(len(row[0]) for row in XY)

        # Build the document tensor. We pad the shorter documents so that all documents
        # have the same length.
        
        Xpadded = torch.as_tensor([row[0] + [pad_id]*(max_sen_len-len(row[0])) for row in XY], device=self.device)
        
        # Build the label tensor.
        Ypadded = torch.as_tensor([row[1] + [pad_id]*(max_sen_len-len(row[1])) for row in XY], device=self.device)

        if len(XY[0]) == 2:
            return Xpadded, Ypadded, None     
        else:
            max_word_len = max(len(w) for _, _, xc in XY for w in xc)
            Xcpadded = [xc + [[]]*(max_sen_len-len(xc)) for _, _, xc in XY]
            Xcpadded = [[w + [pad_id]*(max_word_len-len(w)) for w in xc] for xc in Xcpadded]
            Xcpadded = torch.as_tensor(Xcpadded, device=self.device)            
            return Xpadded, Ypadded, Xcpadded
        
        
from gensim.models import KeyedVectors
import gensim.downloader
import sys
import gensim
import torch

def load_gensim_vectors(model_file, builtin=False, limit=None):
    print(f"Loading model '{model_file}' via gensim...", end='')
    sys.stdout.flush()
    if builtin:
        gensim_model = gensim.downloader.load(model_file)
    else:
        gensim_model = KeyedVectors.load_word2vec_format(model_file, binary=True, limit=limit)
    if not limit:
        limit = len(gensim_model.index2word)
    vectors = torch.FloatTensor(gensim_model.vectors[:limit])
    voc = gensim_model.index2word[:limit]

    is_cased = False
    for w in voc:
        w0 = w[0]
        if w0.isascii() and w0.isupper():
            is_cased = True
            break
    
    print(' done!')
    return vectors, voc, is_cased


# Convert a list of BIO labels, coded as integers, into spans identified by a beginning, an end, and a label.
# To allow easy comparison later, we store them in a dictionary indexed by the start position.
def to_spans(l_ids, vocab):
    spans = {}
    current_lbl = None
    current_start = None
    for i, l_id in enumerate(l_ids):
        l = vocab.itos[l_id]

        if l[0] == 'B': 
            # Beginning of a named entity: B-something.
            if current_lbl:
                # If we're working on an entity, close it.
                spans[current_start] = (current_lbl, i)
            # Create a new entity that starts here.
            current_lbl = l[2:]
            current_start = i
        elif l[0] == 'I':
            # Continuation of an entity: I-something.
            if current_lbl:
                # If we have an open entity, but its label does not
                # correspond to the predicted I-tag, then we close
                # the open entity and create a new one.
                if current_lbl != l[2:]:
                    spans[current_start] = (current_lbl, i)
                    current_lbl = l[2:]
                    current_start = i
            else:
                # If we don't have an open entity but predict an I tag,
                # we create a new entity starting here even though we're
                # not following the format strictly.
                current_lbl = l[2:]
                current_start = i
        else:
            # Outside: O.
            if current_lbl:
                # If we have an open entity, we close it.
                spans[current_start] = (current_lbl, i)
                current_lbl = None
                current_start = None
    return spans

# Compares two sets of spans and records the results for future aggregation.
def compare(gold, pred, stats):
    for start, (lbl, end) in gold.items():
        stats['total']['gold'] += 1
        stats[lbl]['gold'] += 1
    for start, (lbl, end) in pred.items():
        stats['total']['pred'] += 1
        stats[lbl]['pred'] += 1
    for start, (glbl, gend) in gold.items():
        if start in pred:
            plbl, pend = pred[start]
            if glbl == plbl and gend == pend:
                stats['total']['corr'] += 1
                stats[glbl]['corr'] += 1

# This function combines the auxiliary functions we defined above.
def evaluate_iob(words, predicted, gold, vocab, stats):
    
    pad_id = vocab.get_pad_idx()
    padding = list((words == pad_id).reshape(-1).cpu().numpy())
                
    # The gold-standard labels are assumed to be an integer tensor of shape
    # (n_sentences, max_len).
    gold_cpu = gold.cpu().numpy()
    gold_cpu = list(gold_cpu.reshape(-1))

    if not isinstance(predicted, list):        
        pred_flat = predicted.reshape(-1).cpu().numpy()
    else:
        pred_flat = [l for sen in predicted for l in sen]
    pred_flat = [pad_id if is_pad else l for l, is_pad in zip(pred_flat, padding)]
    
    # Compute spans for the gold standard and prediction.
    gold_spans = to_spans(gold_cpu, vocab)
    pred_spans = to_spans(pred_flat, vocab)

    # Finally, update the counts for correct, predicted and gold-standard spans.
    compare(gold_spans, pred_spans, stats)

# Computes precision, recall and F-score, given a dictionary that contains
# the counts of correct, predicted and gold-standard items.
def prf(stats):
    if stats['pred'] == 0:
        return 0, 0, 0
    p = stats['corr']/stats['pred']
    r = stats['corr']/stats['gold']
    if p > 0 and r > 0:
        f = 2*p*r/(p+r)
    else:
        f = 0
    return p, r, f

from IPython.core.display import display, HTML

def show_entities(tagger, sentences):
    
    tagged_sentences = tagger.predict(sentences)

    styles = {
        'LOC': 'background-color: #aaffaa; color: black;',
        'PER': 'background-color: #aaaaff; color: black;',
        'ORG': 'background-color: #ff8800; color: black;',
        'MISC': 'background-color: #00ffff; color: black;'
    }
    content = ['<div style="font-size:150%; line-height: 150%;">']

    for tokens, tags in zip(sentences, tagged_sentences):
        content.append('<div>')
        current_entity = None
        for token, tag in zip(tokens, tags):
            if tag[0] not in ['B', 'I']:
                if current_entity:
                    content.append('</b>')
                    current_entity = None
                content.append(' ')
            elif tag[0] == 'B':
                if current_entity:
                    content.append('</b>')
                content.append(' ')
                current_entity = tag[2:]
                content.append(f'<b style="{styles[current_entity]} border-radius: 3px; padding: 3px;">')
                content.append(f'<sup style=font-size:small;><tt>{current_entity}</tt></sup> ')

            else:
                entity = tag[2:]
                if entity == current_entity:
                    content.append(' ')
                elif current_entity is None:
                    content.append(' ')
                    content.append('<sup style=font-size:small;><tt>[ERROR]</tt></sup> ')
                    content.append(f'<b style="{styles[entity]} border-radius: 3px; padding: 3px;">')
                    content.append(f'<sup style=font-size:small;><tt>{entity}</tt></sup> ')
                else:
                    content.append('</b>')
                    content.append(' ')
                    content.append('<sup style=font-size:small;><tt>[ERROR]</tt></sup> ')
                    content.append(f'<b style="{styles[entity]} border-radius: 3px; padding: 3px;">')
                    content.append(f'<sup style=font-size:small;><tt>{entity}</tt></sup> ')
                current_entity = entity
            content.append(token)
        if current_entity:
            content.append('</b>')
        content.append('</div>')
    content.append('</div>')    
    html = ''.join(content).strip()
    display(HTML(html))
        