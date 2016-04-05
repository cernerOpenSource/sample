#!/usr/bin/env python

import csv
from collections import defaultdict

columns = defaultdict(list) #we want a list to append each value in each column to

with open('textfile.txt') as f:
    reader = csv.reader(f,delimiter=",")
    reader.next()
    for row in reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)
print(columns[0])
print "xfdfdf"
f.close()