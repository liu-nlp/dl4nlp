# Module 3: Structured prediction

This module focuses on architectures and algorithms for NLP tasks where the goal is to predict a structured object such a sequence or a tree. Applications include well-known use cases such as named entity recognition and relation extraction.

## Unit 3-0: Introduction to structured prediction

* Introduction to the module [[slides](slides/module2.pdf)] [[video](https://youtu.be/PK0Kil5REy8)]

**Reading:** Eisenstein, chapter 1

## Unit 3-1: Sequence labelling

* Introduction to sequence prediction tasks [[slides](slides/slides-221.pdf)] [[video](https://youtu.be/VCORDrz-Tzs)]
* Basic models for sequence labeling [[slides](slides/slides-222.pdf)] [[video](https://youtu.be/E7jrhDkrmZQ)]
* Autoregressive sequence models [[slides](slides/slides-231.pdf)] [[video](https://youtu.be/V9TJMODq-rU)]
* Factorized sequence model and the Viterbi algorithm [[slides](slides/slides-232.pdf)] [[video](https://youtu.be/C_5nfLIhMjw)]
* Conditional random fields [[slides](slides/slides-233.pdf)] [[video](https://youtu.be/8wLScZOGeRc)]

**Reading:** Eisenstein, 7.1, 7.6, 8

### Exercise

* Named entity recognition 1 [[code](https://github.com/liu-nlp/dl4nlp/tree/master/exercise2_1)] [[colab](https://drive.google.com/file/d/1xLwc_NGpqscRfJaQAITmE5CoTRqksJAz/view)] [[solution](https://github.com/liu-nlp/dl4nlp/blob/master/exercise2_1/Exercise%202.1%20solution.ipynb)]
* Named entity recognition 2

## Unit 3-2: Syntactic analysis

* Introduction to dependency parsing [[slides](slides/slides-241.pdf)] [[video](https://youtu.be/cx4B43sstTQ)]
* The arc-standard algorithm [[slides](slides/slides-242.pdf)] [[video](https://youtu.be/IQC8Qy8bfG8)]
* The Eisner algorithm [[slides](slides/slides-251.pdf)] [[video](https://youtu.be/QU059k3xifI)]
* Neural parsing architectures [[slides](slides/slides-252.pdf)] [[video](https://youtu.be/l3_HM9NfSjc)]
* Dynamic oracles

**Reading:** Eisenstein, chapter 11

**Reading:** 

* [Chen and Manning (2014)](https://www.aclweb.org/anthology/D14-1082/)
* [Kiperwasser and Goldberg (2016)](https://www.aclweb.org/anthology/Q16-1023/)
* [Dozat and Manning (2017)](https://openreview.net/forum?id=Hk95PK9le)

## Assignment 3

* Introduction to Assignment 2 [[video](https://youtu.be/C7PnsTie1YA)]

[The second programming assignment](assignment2/assignment2.ipynb) is dedicated to the task of *dependency parsing*.

**Reading:** Eisenstein, chapter 18 (where 18.2 is optional)
