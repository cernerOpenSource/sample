import csv
import collections
file = open("userrev.csv","rb")
c1 = csv.reader(file)
unor=[]
i=0
j=0
for row in c1:
    unor.append(row[1])
    j=j+1
b=set(unor)
file.close()
file = open("userrev.csv")
c2 = csv.reader(file)
file1 = open("userrev.csv")
c3 = csv.reader(file1)
import sqlite3
con = sqlite3.connect("PROJECT")
cur = con.cursor()
l=[]
for a in b:
    for row1 in c2:
        if str(a)==str(row1[1]):
            l.append(row[0])
    new=collections.Counter(l)
    l=[]
    for x in new.elements():
        if x>=2:
            print x
            #for z in c3:
             #   if str(a)==str(z[0]):
              #      print z[6]
            #file1.close()
            #file1 = open("userrev.csv")
            #c3 = csv.reader(file1)
            
            #i=i+1
    file.close()
    file = open("userrev.csv")
    c2 = csv.reader(file)
file.close()
    
