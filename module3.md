# Module 3: Structured prediction

This module focuses on architectures and algorithms for NLP tasks where the goal is to predict a structured object such a sequence or a tree. Applications include well-known use cases such as named entity recognition and relation extraction.

## Unit 3-0: Introduction to structured prediction

* Introduction to the module [[slides](slides/module2.pdf)] [[video](https://youtu.be/PK0Kil5REy8)] (44:47)

**Reading:** Eisenstein, chapter 1

**Optional exercise:** [[Biomedical NER](http://www.cse.chalmers.se/~richajo/dat450/assignments/assignment4.html)]

## Unit 3-1: Sequence labelling (94 min)

* Introduction to sequence prediction tasks [[slides](slides/slides-2022-311.pdf)] [[video](https://youtu.be/VCORDrz-Tzs)] (16:48)
* Basic models for sequence labeling [[slides](slides/slides-2022-312.pdf)] [[video](https://youtu.be/E7jrhDkrmZQ)] (13:55)
* Autoregressive sequence models [[slides](slides/slides-2022-313.pdf)] [[video](https://youtu.be/V9TJMODq-rU)] (13:34)
* Factorized sequence model and the Viterbi algorithm [[slides](slides/slides-2022-314.pdf)] [[video](https://youtu.be/C_5nfLIhMjw)] (19:36)
* Conditional random fields [[slides](slides/slides-2022-315.pdf)] [[video](https://youtu.be/8wLScZOGeRc)] (30:56)

**Reading:** Eisenstein, 7.1, 7.6, 8

<!--### Exercises

* Named entity recognition 1 [[code](https://github.com/liu-nlp/dl4nlp/tree/master/exercise2_1)] [[colab](https://drive.google.com/file/d/1xLwc_NGpqscRfJaQAITmE5CoTRqksJAz/view)] [[solution](https://github.com/liu-nlp/dl4nlp/blob/master/exercise2_1/Exercise%202.1%20solution.ipynb)]
* Named entity recognition 2-->

## Unit 3-2: Syntactic analysis (88 min)

* Introduction to dependency parsing [[slides](slides/slides-321.pdf)] [[video](https://youtu.be/8wEOVf-XxmE)] (17:31)
* The arc-standard algorithm [[slides](slides/slides-322.pdf)] [[video](https://youtu.be/YWkf8pUs5zw)] (16:16)
* The Eisner algorithm [[slides](slides/slides-323.pdf)] [[video](https://youtu.be/RPelVqVqctA)] (15:20)
* Neural parsing architectures [[slides](slides/slides-324.pdf)] [[video](https://youtu.be/Y9MAL5dan2I)] (16:08)
* Dynamic oracles [[slides](slides/slides-325.pdf)] [[video](https://youtu.be/epuUR3BzPZo)] (23:10)

**Reading:** Eisenstein, chapter 11

**Reading:** 

* [Chen and Manning (2014)](https://www.aclweb.org/anthology/D14-1082/)
* [Kiperwasser and Goldberg (2016)](https://www.aclweb.org/anthology/Q16-1023/)
* [Dozat and Manning (2017)](https://openreview.net/forum?id=Hk95PK9le)
* [Glavaš and Vulić (2021)](http://dx.doi.org/10.18653/v1/2021.eacl-main.270)

## Schedule for the meeting

| June 2    | June 3   |
|------------|-----------|
|10:15&ndash;12:00: **Discussion**   |9:15&ndash;12:00: **Project presentations**   |
|13:15&ndash;15:00: **Discussion**   |13:15&ndash;15:00: **Assignment** |
|15:15&ndash;17:00: **Exercise**     |15:15&ndash;16:00: **Course recap** |

## Assignment 3

<!--* Introduction to Assignment 3 [[video](https://youtu.be/C7PnsTie1YA)]-->

The [the third programming assignment](https://github.com/liu-nlp/dl4nlp/tree/master/assignment3) is dedicated to the task of *dependency parsing*. More specifically, you will implement a simplified version of the dependency parser used by [Glavaš and Vulić (2021)](http://dx.doi.org/10.18653/v1/2021.eacl-main.270).
