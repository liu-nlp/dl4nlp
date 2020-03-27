# Content of the course

Understanding human language is one of the central goals in artificial
intelligence. Recently, deep learning approaches have revolutionized
the field, and define the state of the art for many different natural
language processing (NLP) tasks, including commerically important
applications such as translation, summarization, and information
extraction. However, natural language data exhibit a number of
peculiarities that make them more challenging to work with than many
other types of data commonly encountered in machine learning: natural
language is discrete, structured, and highly ambiguous. It is
extremely diverse: not only are there thousands of languages in the
world, but in each language there is substantial variation in style
and genre. Furthermore, many of the phenomena encountered in language
follow long-tail statistical distributions, which makes the production
of training data more costly. For these reasons, machine learning
architectures for NLP applications tend to be quite different from
those used in other fields.

The goal of the course is to give participants the theoretical
knowledge and practical experience required to use state-of-the-art
natural language processing in their own research – for example, to
integrate existing software components for natural language
understanding into an autonomous system, or to understand, implement,
and evaluate a cutting-edge deep learning architecture based on its
description in a research article.

The following is a preliminary overview of the topics we will try to
cover in the course.

# Part 1: Introduction to deep learning and NLP; representations for NLP; categorization

The first module covers fundamental concepts in NLP and deep learning
models. We first discuss NLP as a research area, including a quick
overview of the history of the field, and highlight the particular
challenges of building machine learning models for language processing
problems. We will then discuss fundamental notions in​ representation
learning for NLP​, including representations of words and larger units,
and the opportunities for pre-training and transfer learning in
NLP. Finally, we will consider the family of NLP tasks that can be
cast as text categorization problems​, and see a number of deep
learning architectures for this class of problems. This module will
also include a quick practical refresher of general deep learning
architectures and libraries.

# Part 2: Structured prediction problems in NLP

The second part is focused on NLP problems that require an automatic
system to convert a text into a structured format: ​structured
prediction problems​. This family of tasks ranges from structurally
simple problems such as sequence tagging to complex prediction tasks
where a tree or graph needs to be produced by the system. We will
first focus on sequence tagging problems of the type normally
encountered in information extraction, such as named entity
recognition, and see a number of deep learning architectures for
sequence prediction tasks, including models such as recurrent neural
networks and conditional random fields. We will then consider
structured prediction more generally, and discuss different approaches
to casting structured prediction problems as machine learning tasks,
and the challenges of training such models. A number of complex
prediction tasks will be highlighted, such as dependency parsing and
relation extraction.

# Part 3: Generation problems in NLP

The third part focuses on​ generation problems​: NLP tasks that require
the system to produce free text. The most well-known problem of this
type is probably machine translation, and this use case will be
discussed extensively. We will introduce deep learning architectures
for translation tasks, including the famous sequence-to-sequence and
attention models. The module will also discuss a number of additional
generation tasks, including text summarization and generation for
dialogue systems. We will also consider multimodal generation tasks,
such as image captioning.
