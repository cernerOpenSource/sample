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
def sentencetokenize(reader):
    #line=reader.readLine()
    
    fo=open("sentence.txt","a+")
    for line in reader: 
        fo.write('\n'.join(PunktSentenceTokenizer().tokenize(line[2])))
        
        
    fo.close()
        

def processReview(review):
    # process the tweets
 
    #Convert to lower case
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
    fo=open("clean.txt","a+")
    fo.write(review)
    fo.write("\n")
    fo.close()
    return review
#end

def shorthanddata(reader):
    line=reader.readline()
    fo=open("expansion.txt","a+")
    while line:
        fo.write(replacer.replace(line))
        line=reader.readline()
    fo.close()
        
def wordtokenize(reader):
    line=reader.readline()
    fo=open("words.txt","a+")
    while line:
        fo.write('\n'.join(word_tokenize(line)))
        fo.write('\n')
        line=reader.readline()
    fo.close()


def stopwords(reader):
    line=reader.readline()
    fo=open("wordswithoutstopwords.txt","a+")
   #while line:
    while line:
        if line not in '\n'.join(english_stops):
            fo.write(line)
        line=reader.readline() 
    fo.close()
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
def stemy(reader):
    
    fo=open("stemming.txt","a+")
    for line in reader:
      # for word in line.split():
       #     print stemmer.stem(word)
       #x=repr(line)
        #print stemmer.stem("dogs")
        #a=stemmer.stem(x.rstrip('\r\n'))
       
        a= stemmer.stem()
        print a
        #print stemmer.stem(str(line))
       
        fo.write(a)
    fo.close()
def stemreplacer(reader):
    line=reader.readline()
    replacer = SpellingReplacer()
    fo=open("stemreplacer.txt","a+" )
    while line:
        fo.write(replacer.replace(line))
        line=reader.readline()
    fo.close()
def antonymfilter(reader):
    line=reader.readline()
    fo=open("finalfile.txt","a+" )
    while line:
        if(not wordnet.synsets(line)):
            fo.write(line)
        else:
            l=wordnet.synsets(line)[0].lemmas[0]
            fo.write(l.name)
        line=reader.readline()
    fo.close()    
file = open("saibaba.csv")
reader = csv.reader(file)
sentencetokenize(reader)
fp1 = open('sentence.txt', 'r')
line=fp1.readline()
while line:
    
    line=fp1.readline()
fp2 = open('clean.txt', 'r')
shorthanddata(fp2)
fp3=open('expansion.txt','r')
wordtokenize(fp3)
fp4=open('words.txt','r')
stopwords(fp4)
fp5=open('wordswithoutstopwords.txt','r')
stemy(fp5)
fp6=open("stemming.txt",'r')
stemreplacer(fp6)
fp7=open("stemreplacer.txt","a+")
antonymfilter(fp7)




 


