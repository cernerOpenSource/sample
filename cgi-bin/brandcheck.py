#!/usr/bin/env python
import csv
from collections import Counter
with open('newdata.csv', 'rb') as newf, open('product.csv','rb') as pro:
    old_reader = csv.reader(newf)
    new_reader=csv.reader(pro)
    i=1
    for row in old_reader:
        for col in new_reader :
            if(row[0]==col[0]):
                list.append(col[1])
        if row[0]=="new user":
            c=Counter(list)
            a=max(c)
            b=len(list)
            c=(a/b)*100
            if c>=50:
                