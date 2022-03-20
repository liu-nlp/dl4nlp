# Module 2: Foundation models

Modern NLP architectures are based on general-purpose models that are trained on large amounts of broad-coverage data and are adaptable to a wide range of downstream tasks. This module introduces the basic ideas behind these models and their use for practical applications.

## Unit 2-1: Transformer models (72 min)

* Introduction to machine translation
* Neural machine translation
* Attention [[slides](slides/slides-163.pdf)] [[video](https://youtu.be/Ft1J79L11oU)] (14:52)
* The Transformer architecture
* BERT and other pre-trained transformer models

* Introduction to generation tasks [[slides](slides/slides-311.pdf)] [[video](https://youtu.be/rQgA09R8kSM)] (12:36)
* Evaluation of generation systems [[slides](slides/slides-312.pdf)] [[video](https://youtu.be/pJHmKn2FDRY)] (20:43)
* Introduction to machine translation [[slides](slides/slides-313.pdf)] [[video](https://youtu.be/_4F9cXe7dWc)] (24:26)
* Recent developments in machine translation

**Reading:**

* Eisenstein, chapter 6
* Papers on attention: [Cheng et al. (2016)](https://www.aclweb.org/anthology/D16-1053/), [Vaswani et al. (2017)](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf), [Serrano and Smith (2019)](https://www.aclweb.org/anthology/D18-1216/)

## Unit 2-2: Transfer learning (59 min)

* Transfer learning in NLP: static and contextualized representations [[slides](slides/slides-171.pdf)] [[video](https://youtu.be/2Lo1U-O9Ta4)] (08:08)
* Language models for pre-training [[slides](slides/slides-172.pdf)] [[video](https://youtu.be/GFG38b0CKS0)] (20:13)
* The Transformer model [[slides](slides/slides-173.pdf)] [[video](https://youtu.be/Wtlxh2-JWq8)] (12:51)
* Pre-trained Transformer models [[slides](slides/slides-174.pdf)] [[video](https://youtu.be/BEYeBd5Gxc0)] (18:12)

**Examples:**
* Document classification using BERT [[notebook](http://www.cse.chalmers.se/~richajo/waspnlp2020/m1_7/Document%20classification%20with%20BERT.ipynb)] [[colab](https://drive.google.com/file/d/1SS_IB07kcbRGdIhbQCGMwd70TDPh9eqH/view?usp=sharing)]

**Reading:**
* [NLP's ImageNet moment has arrived](https://ruder.io/nlp-imagenet/)
* [The illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)
* [The illustrated BERT, ELMo, and co.](http://jalammar.github.io/illustrated-bert/)
* Papers: [Peters et al. (2018)](https://arxiv.org/abs/1802.05365), [Devlin et al. (2019)](https://arxiv.org/abs/1810.04805)

## Assignment 2

* Machine translation [[code](https://github.com/liu-nlp/dl4nlp/tree/master/exercise3_1)] [[colab](https://drive.google.com/file/d/1sjw6F1V1ruIc02mejKMq1cdYyU56u3i4/view?usp=sharing)] [[solution](https://github.com/liu-nlp/dl4nlp/blob/master/exercise3_1/Machine%20Translation%20Exercise%20(solution).ipynb)]

## Random stuff

This lecture consists of two external videos on other generation problems.

* Natural Language Generation (Abigail See) [[video](https://www.youtube.com/watch?v=4uG1NMKNWCU)]
* Models of Dialog (Graham Neubig) [[video](https://www.youtube.com/watch?v=ytTwIgdSnVU)]

**Reading:** Eisenstein, chapter 19
