# -*- coding: utf-8 -*-
"""
Created on Thu May 05 11:02:46 2016

@author: Francisc
"""

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#free contents from nltk, the following are from the state of the union address of George W. Bush
train_set = state_union.raw('2005-GWBush.txt')
test_set = state_union.raw('2006-GWBush.txt')

#tokenizing the training set, splitting them according to the punktsentencetokenizer algorithm
custom_sent_tokenizer = PunktSentenceTokenizer(train_set)

#tokenizing and testing with the test set
tokenized = custom_sent_tokenizer.tokenize(test_set)


def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary = True)
            namedEnt.draw()
            
    except Exception as e:
        print(str(e))

process_content()