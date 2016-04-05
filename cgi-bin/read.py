#!c:\Python27\python.exe
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
# open and read the csv file into memory
file = open("saibaba.csv")
reader = csv.reader(file)
# iterate through the lines and print them to stdout
# the csv module returns us a list of lists and we
# simply iterate through it
replacer = SpellingReplacer()
fo1=open("c-expansion.txt","a+")

fo6=open("h-synset.txt","a+")
fo5=open("g-spellcheck.txt","a+")
fo4=open("f-stemmingwords.txt","a+")
fo3=open("e-wordswithoutstopwords.txt","a+")
fo2=open("d-words.txt","a+")
fo=open("a-sentence.txt","a+")
for line in reader:
    a= PunktSentenceTokenizer().tokenize(line[2])
    fo.write('\n'.join(a))
    review='\n'.join(a)
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
    fo7=open("b-clean.txt","a+")
    fo7.write(review+"\n")
    q=replacer.replace(review)
    fo1.write(q)
    z= PunktSentenceTokenizer().tokenize(q)
    for m in z:
        b=word_tokenize(m)
        fo2.write('\n'.join(b)+"\n")
        
        for j in b:
            if j not in '\n'.join(english_stops):
                fo3.write(j+"\n")
                
                
            else:
                continue
            f=stemmer.stem(j)
            fo4.write(f+"\n")
            g=replacer.replace(f)
            fo5.write(g+"\n")
            if(not wordnet.synsets(g)):
                fo6.write(g+"\n")
            else:
                h=wordnet.synsets(g)[0].lemmas[0]
                fo6.write(h.name+"\n")
            
        
        
fo1.close()
fo.close()
fo2.close()
fo3.close()
fo4.close()
fo5.close()
fo6.close()
fo7.close()
