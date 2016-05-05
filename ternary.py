# -*- coding: utf-8 -*-
"""
Created on Thu May 05 17:05:11 2016

@author: Francisc
"""

import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
                 
print(documents[:5])