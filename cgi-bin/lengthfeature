#!/usr/bin/env python
import csv
import collections
import sqlite3
import nltk
import numpy
file = open("userrev.csv","rb")
c = csv.reader(file)
i=0
a=[]
total=0
for row in c:
    total=total+len(row[6])
    
    i=i+1
i=i-1
mean=total/i
print mean
file.close()
file = open("userrev.csv","rb")
c = csv.reader(file)
for col in c:
    l=len(col[6])
    if l<=mean/2:
       a.append(col[0])
fakereviewer=set(a)
x=0
for k in fakereviewer:
    x=x+1
    print k
print x
file.close()
