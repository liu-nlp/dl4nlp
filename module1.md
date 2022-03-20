# Module 1: Word representations

This module introduces one of the most fundamental ideas in modern NLP: the idea that words can be represented as vectors which can be learned from text data. On the application side of things, we focus on one of the most fundamental NLP tasks: text categorization.

## Unit 1-1

* Representing documents for neural networks [[slides](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/m3_1.pdf)] [[video](https://youtu.be/xsQ46CXsIfc)]
* Introduction to embeddings [[slides](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/m3_2.pdf)] [[video](https://youtu.be/LLUjsmuEgk8)]
* Continuous bag-of-words representations [[slides](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/m3_3.pdf)] [[video](https://youtu.be/MOcGoA3Fbi8)]
* Examples [[notebook](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/Document%20classification.ipynb)] [[colab](https://drive.google.com/file/d/1VLIAYXSoLN99BwS9CUTJYS7caazBVORF/view?usp=sharing)] [[video](https://youtu.be/ZEYESgSR29o)]

**Reading:** Goldberg, chapter 8; [Joulin et al. (2017)](https://aclweb.org/anthology/E17-2068)

## Exercise 2

* Text categorization and word embeddings [[notebook]](http://www.cse.chalmers.se/~richajo/waspnlp2020/ex1_2/ex1_2.html) [[video](https://www.youtube.com/watch?v=pcVh5Ga3JmM)] [[solution](http://www.cse.chalmers.se/~richajo/waspnlp2020/ex1_2/Exercise%201.2%20-%20solution.ipynb)]

## Unit 1-2: Word embeddings

* Pre-training word embedding models: introduction [[slides](slides/slides-141.pdf)] [[video](https://youtu.be/6AozaHmWugs)]
* The SGNS algorithm [[slides](slides/slides-142.pdf)] [[video](https://youtu.be/R5EhgHz2S5w)]
* Evaluation and interpretation of word embeddings [[slides](slides/slides-143.pdf)] [[video](https://youtu.be/gcWF3AIUtJ8)]
* More training algorithms for word embeddings [[slides](slides/slides-144.pdf)] [[video](https://youtu.be/TMHI-Dk3c44)]
* Perspectives [[slides](slides/slides-145.pdf)] [[video](https://youtu.be/XxI7fb7aabU)]
* Subword representations [[slides](slides/slides-223.pdf)] [[video](https://youtu.be/1ZDpYspEM_M)]

**Examples**
* Using Gensim: [[notebook](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_4/Word%20embeddings%20in%20Gensim.ipynb)] [[colab](https://drive.google.com/file/d/1CE37dcmGRIbUtuAoTruzzuGAnboeyaVh/view?usp=sharing)]
* SGNS implementation in PyTorch: [[notebook](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_4/Skip-gram%20with%20negative%20sampling.ipynb)] [[colab](https://drive.google.com/file/d/1_ian039WL__VdYaW6PoOtcgHkdlUlsOJ/view?usp=sharing)]

**Reading:** Goldberg, chapter 10–11; [Schnabel et al. (2015)](https://www.aclweb.org/anthology/D15-1036.pdf)

## Unit 1-3:

* Convolutional neural networks [[slides](slides/slides-151.pdf)] [[video](https://youtu.be/8sUa97gYNDE)]
* Recurrent neural networks [[slides](slides/slides-152.pdf)] [[video](https://youtu.be/cswaoJvJass)]
* The LSTM architecture [[slides](slides/slides-153.pdf)] [[video](https://youtu.be/YVvW9i_BhEg)]

**Reading:** Goldberg, chapters 13–15

## Unit 1-4: Contextualized word embeddings

* Introduction to language modelling
* N-gram language models
* Recurrent neural networks
* The LSTM architecture
* Recurrent neural network language models
* Contextualized word embeddings

* Language modelling [[slides](slides/slides-161.pdf)] [[video](https://youtu.be/EeVQzalQp2I)]
* N-gram language models [[slides](slides/slides-162.pdf)] [[video](https://youtu.be/QcZpgBzQlBg)]

## Exercise 3

**Form:** Scheduled, 23 April, 15:15–17:00, Zoom.

* Language modelling [[notebook](https://github.com/liu-nlp/dl4nlp/tree/master/exercise3)] [[video](https://youtu.be/UPmQQwfNKfg)] [[solution](https://github.com/liu-nlp/dl4nlp/tree/master/exercise3)]

## Programming assignment

[The first programming assignment](http://www.cse.chalmers.se/~richajo/waspnlp2020/a1/assignment1.html) is dedicated to the task of *word sense disambiguation*.

We have a scheduled QA session about the assignment: 17 April, 16:00–17:00, Zoom.
