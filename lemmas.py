# -*- coding: utf-8 -*-
"""
Created on Thu May 05 14:33:01 2016

@author: Francisc
"""

from nltk.corpus import wordnet

syns = wordnet.synsets("tumultuous")

print(syns[0].lemmas()[0].name())