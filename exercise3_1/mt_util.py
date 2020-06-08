def read_lines(filename, max_lines=None, max_sen_length=None):
    with open(filename) as f:
        out = []
        for i, l in enumerate(f):
            if i == max_lines:
                break
            sen = l.strip().split()
            if max_sen_length:
                sen = sen[:max_sen_length]
            out.append(sen)
        return out

from collections import defaultdict, Counter    
import torch
from torch import nn

PAD = '*PAD*'
UNKNOWN = '*UNK*'
BOS = '*BOS*'
EOS = '*EOS*'

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
            self.itos = self.dummies + [ w for _, w in word_freqs[:self.max_voc_size-len(self.dummies)] ]
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

    def decode(self, seqs):
        return [[self.itos[wi] for wi in seq] for seq in seqs]
        
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
        max_X_len = max(len(row[0]) for row in XY)
        max_Y_len = max(len(row[1]) for row in XY)

        # Build the document tensor. We pad the shorter documents so that all documents
        # have the same length.
        
        Xpadded = torch.as_tensor([row[0] + [pad_id]*(max_X_len-len(row[0])) for row in XY], device=self.device)
        
        # Build the label tensor.
        Ypadded = torch.as_tensor([row[1] + [pad_id]*(max_Y_len-len(row[1])) for row in XY], device=self.device)

        if len(XY[0]) == 2:
            return Xpadded, Ypadded
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
        if w0.isupper():
            is_cased = True
            break
    
    print(' done!')
    return vectors, voc, is_cased

