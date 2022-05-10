# Module 2: Foundation models

Modern NLP architectures are based on general-purpose models that are trained on large amounts of broad-coverage data and are adaptable to a wide range of downstream tasks. This module introduces the basic ideas behind these models and their use for practical applications.

## Unit 2-1: Introduction to generation and translation (68 min)

* Introduction to generation tasks [[slides](slides/slides-211.pdf)] [[video](https://youtu.be/rQgA09R8kSM)] (12:36)
* Evaluation of generation systems [[slides](slides/slides-212.pdf)] [[video](https://youtu.be/pJHmKn2FDRY)] (20:43)
* Introduction to machine translation [[slides](slides/slides-213.pdf)] [[video](https://youtu.be/P5KMKApthuM)] (18:25)
* Neural machine translation [[slides](slides/slides-214.pdf)] [[video](https://youtu.be/BqKbbygwsVc)] (16:29)

**Reading:**

* Eisenstein, chapter 6

## Unit 2-2: Transformer models (71 min)

* Attention [[slides](slides/slides-221.pdf)] [[video](https://youtu.be/HHUR6VX5CeU)] (15:13)
* The Transformer architecture [[slides](slides/slides-222.pdf)] [[video](https://youtu.be/dSd0-RFZLnk)] (13:43)
* Pre-trained transformer models 1 (GPT) [[slides](slides/slides-223.pdf)] [[video](https://youtu.be/9QE1bQTSbx8)] (22:53)
* Pre-trained transformer models 2 (BERT) [[slides](slides/slides-224.pdf)] [[video](https://youtu.be/JeY6N1012Sg)] (18:59)

**Reading:**

* [Cheng et al. (2016)](https://www.aclweb.org/anthology/D16-1053/)
* [Vaswani et al. (2017)](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)
* [Serrano and Smith (2019)](https://www.aclweb.org/anthology/D18-1216/)
* [Radford et al. (2018)](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)
* [Devlin et al. (2019)](dx.doi.org/10.18653/v1/N19-1423)

## Unit 2-3: More applications of generation (55 min)

* Summarization [[slides](http://www.cse.chalmers.se/~richajo/dat450/lectures/l12/l12_1.pdf)] [[video](https://youtu.be/EUJlrdJhBJg)]
* Dialogue systems [[slides](slides/slides-2022-232.pdf)] [[video](https://youtu.be/jWkQLVN3ixI)]

**Reading:**
* [Eisenstein](https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf), chapter 19
* [Roller et al (2021)](https://aclanthology.org/2021.eacl-main.24/)

## Unit 2-4: Out-of distribution scenarios and domain adaptation (54 min)

* Introduction to domain adaptation [[slides](http://www.cse.chalmers.se/~richajo/dat450/lectures/l13/l13_1.pdf)] [[video](https://youtu.be/C-Liu_qvavY)]
* Domain-adversarial training [[slides](http://www.cse.chalmers.se/~richajo/dat450/lectures/l13/l13_2.pdf)] [[video](https://youtu.be/Ei9JY06nepo)]
* Pseudo-labeling for domain adaptation [[slides](http://www.cse.chalmers.se/~richajo/dat450/lectures/l13/l13_3.pdf)] [[video](https://youtu.be/us7l7xvGQ-U)]
* Fine-tuning for adaptation [[slides](slides/slides-2022-244.pdf)] [[video](https://youtu.be/_s8zi_rFjyI)]

**Reading:**
* [Plank and Ramponi (2020)](https://aclanthology.org/2020.coling-main.603/)

## Schedule for the meeting

[Zoom link](https://liu-se.zoom.us/j/65824605892?pwd=RjdwUCtBRnh2YzA1MENEOSt4V2o3QT09)

| May 9    | May 10   |
|------------|-----------|
|9:15&ndash;10:00: **Assignment recap**  |9:15&ndash;10:00:  **Discussion** |
|10:15&ndash;12:00: **Discussion**   |10:15&ndash;12:00: **[Exercise](https://drive.google.com/file/d/1wavzFlUFyeybqUe9iLU_5QWhbwHMNL4s/view?usp=sharing)**   |
|13:15&ndash;15:00: **[Exercise](https://drive.google.com/file/d/17hVSNA2xjZLOJm_qapSeaC7dDnaqvwAi/view?usp=sharing)**     |13:15&ndash;14:00: **Guest talk** |
|15:15&ndash;17:00: **Discussion**   |14:15&ndash;16:00: **Assignment** |
|                                    |16:15&ndash;17:00: **Project**    |

## Exercises

* Exercise 1: [Using BERT models](https://drive.google.com/file/d/17hVSNA2xjZLOJm_qapSeaC7dDnaqvwAi/view?usp=sharing)
* Exercise 2: [Generation](https://drive.google.com/file/d/1wavzFlUFyeybqUe9iLU_5QWhbwHMNL4s/view?usp=sharing)

## Assignment 2

In [the second programming assignment](https://github.com/liu-nlp/dl4nlp/tree/master/assignment2) you will implement the encoder–decoder architecture of Sutskever et al. (2014), including the attention-based extension of Bahdanau et al. (2015), and evaluate this architecture on a machine translation task.

**Deadline: 2022-05-20**
