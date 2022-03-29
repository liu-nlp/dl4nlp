# Module 1: Word representations

This module introduces one of the most fundamental ideas in modern NLP: the idea that words can be represented as vectors which can be learned from text data. On the application side of things, we focus on one of the most fundamental NLP tasks: text categorization.

Before working with the material in this module, you may want to have a look at the following:

* Capsule introduction to NLP [[slides](slides/intro.pdf)] [[video](https://youtu.be/6u7u1cpVT7Y)]
* [Review materials](review.md)

## Unit 1-1: Introduction (56 min)

* Representing documents for neural networks [[slides](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/m3_1.pdf)] [[video](https://youtu.be/xsQ46CXsIfc)] (07:07)
* Introduction to embeddings [[slides](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/m3_2.pdf)] [[video](https://youtu.be/LLUjsmuEgk8)] (09:43)
* Continuous bag-of-words representations [[slides](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/m3_3.pdf)] [[video](https://youtu.be/MOcGoA3Fbi8)] (11:05)
* Examples [[notebook](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/Document%20classification.ipynb)] [[colab](https://drive.google.com/file/d/1VLIAYXSoLN99BwS9CUTJYS7caazBVORF/view?usp=sharing)] [[video](https://youtu.be/ZEYESgSR29o)] (28:46)

**Reading:** Goldberg, chapter 8; [Joulin et al. (2017)](https://aclweb.org/anthology/E17-2068)

## Unit 1-2: Pre-training word embeddings

<!--* Text categorization and word embeddings [[notebook]](http://www.cse.chalmers.se/~richajo/waspnlp2020/ex1_2/ex1_2.html) [[video](https://www.youtube.com/watch?v=pcVh5Ga3JmM)] (55:52)-->

* Pre-training word embedding models: introduction [[slides](slides/slides-141.pdf)] [[video](https://youtu.be/6AozaHmWugs)] (15:06)
* The SGNS algorithm [[slides](slides/slides-142.pdf)] [[video](https://youtu.be/R5EhgHz2S5w)] (09:21)
* Evaluation and interpretation of word embeddings [[slides](slides/slides-143.pdf)] [[video](https://youtu.be/gcWF3AIUtJ8)] (19:17)
* More training algorithms for word embeddings [[slides](slides/slides-144.pdf)] [[video](https://youtu.be/TMHI-Dk3c44)] (22:23)
<!--* Perspectives [[slides](slides/slides-145.pdf)] [[video](https://youtu.be/XxI7fb7aabU)] (16:19)-->
* Subword representations [[slides](slides/slides-223.pdf)] [[video](https://youtu.be/1ZDpYspEM_M)] (13:50)

**Examples**
* Using Gensim: [[notebook](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_4/Word%20embeddings%20in%20Gensim.ipynb)] [[colab](https://drive.google.com/file/d/1CE37dcmGRIbUtuAoTruzzuGAnboeyaVh/view?usp=sharing)]
* SGNS implementation in PyTorch: [[notebook](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_4/Skip-gram%20with%20negative%20sampling.ipynb)] [[colab](https://drive.google.com/file/d/1_ian039WL__VdYaW6PoOtcgHkdlUlsOJ/view?usp=sharing)]

**Reading:** Goldberg, chapter 10–11; [Schnabel et al. (2015)](https://www.aclweb.org/anthology/D15-1036.pdf)

## Unit 1-3: Language modelling and contextualized embeddings

### Lectures

* Introduction to language modelling [[slides](slides/slides-121.pdf)] [[video](https://youtu.be/_TlvRtoGOn8)] (15:03)
* N-gram language models [[slides](slides/slides-122.pdf)] [[video](https://youtu.be/GuTAMrqiFSM)] (16:35)
* Recurrent neural networks [[slides](slides/slides-123.pdf)] [[video](https://youtu.be/RWxoiA2uGZU)] (18:34)
* The LSTM architecture [[slides](slides/slides-124.pdf)] [[video](https://youtu.be/8es6TKvw7qI)] (12:55)
* Recurrent neural network language models [[slides](slides/slides-125.pdf)] [[video](https://youtu.be/J-KglYsuJ28)] (11:14)
* Contextualized word embeddings [[slides](slides/slides-126.pdf)] [[video](https://youtu.be/5oXWnSBoe7A)] (13:00)

### Reading

Goldberg, chapters 13–15

### Exercises (on-site)

* Recurrent neural networks
* Recurrent neural network language models

## Assignment 1

[The first programming assignment](http://www.cse.chalmers.se/~richajo/waspnlp2022/a1/assignment1.html) is dedicated to the task of *word sense disambiguation*.
