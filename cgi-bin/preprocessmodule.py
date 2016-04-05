#!/usr/bin/env python

import re
from nltk.corpus import stopwords
from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.tokenize import word_tokenize
from replacers import RegexpReplacer
replacer = RegexpReplacer()
import csv
from nltk.corpus import wordnet
from nltk.tokenize.punkt import PunktSentenceTokenizer
from replacers import SpellingReplacer
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
def sentence(s):
    a= PunktSentenceTokenizer().tokenize(s)
    return a
def filterreview(s):
    review='\n'.join(s)
    review = review.lower()
    #Convert www.* or https?://* to URL
    review = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',review)
    #Convert @username to AT_USER
    review = re.sub('@[^\s]+','AT_USER',review)
    #Remove additional white spaces
    review = re.sub('[\s]+', ' ', review)
    #Replace #word with word
    review = re.sub(r'#([^\s]+)', r'\1', review)
    review=re.sub('\.',' ',review)
    review=re.sub('\!','',review)
    review=re.sub('\,','',review)
    #trim
    review = review.strip('\'"')
    return review

def expansion(s):
    q=replacer.replace(s)
    return q
def words(s):
    z= PunktSentenceTokenizer().tokenize(s)
    for m in z:
        b=word_tokenize(m)

    
    
    
    
