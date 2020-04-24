# Module 1

In the first module, we introduce the most important building blocks used in modern NLP architectures. We will also consider one of the most fundamental NLP tasks: text categorization.

## Review

We assume that you have background knowledge in machine learning and neural networks and practical exposure to PyTorch. If you need to brush up this up a bit, then you can look at the following background/review material:

* Machine learning basics, deep feedforward networks [[playlist](https://www.youtube.com/playlist?list=PLvWwkcdbWwLWq2H9Zs1Ze91oE0kJN8OD_)]
* PyTorch 60 Minute Blitz [[tutorial](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)]
* Neural models with PyTorch [[videos](https://www.youtube.com/watch?v=XqUCkf7Muuw&list=PLvWwkcdbWwLVi7Nb9RK410ApKdHsHhxtO&index=3&t=0s)] [[notebook and data](https://github.com/liu-nlp/dl4nlp/tree/master/background)]

**Reading:** Goldberg, chapter 1–7 (review)

## Lecture 1

**Form:** Scheduled, 30 March, 13:15–14:00, Zoom

* Welcome!
* Course overview, practical matters [[slides](slides/intro.pdf)] [[video](https://www.ida.liu.se/~marku61/tmp/introduction.mp4)]
* Capsule introduction to NLP [[slides](slides/slides-111.pdf)] [[video](https://youtu.be/6u7u1cpVT7Y)]

**Reading:** Eisenstein, chapter 1

## Lecture 2

**Form:** Self-study

* Essentials of linguistics [[slides](slides/slides-121.pdf)] [[video](https://youtu.be/riYFhZj_CMg)]
* Introduction to text classification [[slides](slides/slides-122.pdf)] [[video](https://youtu.be/3yeOoKhiy8A)]
* Evaluation of text classifiers [[slides](slides/slides-123.pdf)] [[video](https://youtu.be/YPq1Ztr-AAI)]

**Reading:** Eisenstein, sections 2.1, 2.3, 2.5, 2.6; chapter 4

## Exercise 1

**Form:** Scheduled, 31 March, 10:15–12:00, Zoom

* Working with text [[notebook](https://github.com/liu-nlp/dl4nlp/tree/master/exercise1)] [[video](https://youtu.be/WgExvhBMHUU)]

## Lecture 3

**Form:** Self-study

* Representing documents for neural networks [[slides](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/m3_1.pdf)] [[video](https://youtu.be/xsQ46CXsIfc)]
* Introduction to embeddings [[slides](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/m3_2.pdf)] [[video](https://youtu.be/LLUjsmuEgk8)]
* Continuous bag-of-words representations [[slides](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/m3_3.pdf)] [[video](https://youtu.be/MOcGoA3Fbi8)]
* Examples [[notebook](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_3/Document%20classification.ipynb)] [[colab](https://drive.google.com/file/d/1VLIAYXSoLN99BwS9CUTJYS7caazBVORF/view?usp=sharing)] [[video](https://youtu.be/ZEYESgSR29o)]

**Reading:** Goldberg, chapter 8; [Joulin et al. (2017)](https://aclweb.org/anthology/E17-2068)

## Exercise 2

**Form:** Scheduled, 9 April, 10:15–12:00, Zoom

* Text categorization and word embeddings [[notebook]](http://www.cse.chalmers.se/~richajo/waspnlp2020/ex1_2/ex1_2.html) [[video](https://www.youtube.com/watch?v=pcVh5Ga3JmM)] [[solution](http://www.cse.chalmers.se/~richajo/waspnlp2020/ex1_2/Exercise%201.2%20-%20solution.ipynb)]

## Lecture 4

**Form:** Self-study

* Pre-training word embedding models: introduction [[slides](slides/slides-141.pdf)] [[video](https://youtu.be/6AozaHmWugs)]
* The SGNS algorithm [[slides](slides/slides-142.pdf)] [[video](https://youtu.be/R5EhgHz2S5w)]
* Evaluation and interpretation of word embeddings [[slides](slides/slides-143.pdf)] [[video](https://youtu.be/gcWF3AIUtJ8)]
* More training algorithms for word embeddings [[slides](slides/slides-144.pdf)] [[video](https://youtu.be/TMHI-Dk3c44)]
* Perspectives [[slides](slides/slides-145.pdf)] [[video](https://youtu.be/XxI7fb7aabU)]

**Examples**
* Using Gensim: [[notebook](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_4/Word%20embeddings%20in%20Gensim.ipynb)] [[colab](https://drive.google.com/file/d/1CE37dcmGRIbUtuAoTruzzuGAnboeyaVh/view?usp=sharing)]
* SGNS implementation in PyTorch: [[notebook](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_4/Skip-gram%20with%20negative%20sampling.ipynb)] [[colab](https://drive.google.com/file/d/1_ian039WL__VdYaW6PoOtcgHkdlUlsOJ/view?usp=sharing)]

**Reading:** Goldberg, chapter 10–11; [Schnabel et al. (2015)](https://www.aclweb.org/anthology/D15-1036.pdf)

## Lecture 5

**Form:** Self-study

* Convolutional neural networks [[slides](slides/slides-151.pdf)] [[video](https://youtu.be/8sUa97gYNDE)]
* Recurrent neural networks [[slides](slides/slides-152.pdf)] [[video](https://youtu.be/cswaoJvJass)]
* The LSTM architecture [[slides](slides/slides-153.pdf)] [[video](https://youtu.be/YVvW9i_BhEg)]

**Reading:** Goldberg, chapters 13–15

## Lecture 6

**Form:** Self-study

* Language modelling [[slides](slides/slides-161.pdf)] [[video](https://youtu.be/EeVQzalQp2I)]
* N-gram language models [[slides](slides/slides-162.pdf)] [[video](https://youtu.be/QcZpgBzQlBg)]
* Neural language models
* Attention models

**Reading:**  Eisenstein, chapter 6

## Lecture 7

**Form:** Self-study
* Transfer learning in NLP: static and contextualized representations [[slides](slides/slides-171.pdf)] [[video](https://youtu.be/2Lo1U-O9Ta4)]
* Language models for pre-training [[slides](slides/slides-172.pdf)] [[video](https://youtu.be/GFG38b0CKS0)]
* The Transformer model [[slides](slides/slides-173.pdf)] [[video](https://youtu.be/Wtlxh2-JWq8)]
* Pre-trained Transformer models [[slides](slides/slides-174.pdf)] [[video](https://youtu.be/BEYeBd5Gxc0)]

**Examples:**
* Document classification using BERT [[notebook](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_7/Document%20classification%20with%20BERT.ipynb)] [[colab](https://drive.google.com/file/d/1SS_IB07kcbRGdIhbQCGMwd70TDPh9eqH/view?usp=sharing)]

**Reading:**
* [NLP's ImageNet moment has arrived](https://ruder.io/nlp-imagenet/)
* [The illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)
* [The illustrated BERT, ELMo, and co.](http://jalammar.github.io/illustrated-bert/)
* Papers: [Peters et al. (2018)](https://arxiv.org/abs/1802.05365), [Devlin et al. (2019)](https://arxiv.org/abs/1810.04805)

## Exercise 3

**Form:** Scheduled, 23 April, 15:15–17:00, Zoom.

* Language modelling [[notebook](https://github.com/liu-nlp/dl4nlp/tree/master/exercise3)] [[video](https://youtu.be/UPmQQwfNKfg)] [[solution](https://github.com/liu-nlp/dl4nlp/tree/master/exercise3)]

## Programming assignment

[The first programming assignment](http://www.cse.chalmers.se/~richajo/waspnlp2020/a1/assignment1.html) is dedicated to the task of *word sense disambiguation*.

We have a scheduled QA session about the assignment: 17 April, 16:00–17:00, Zoom.
