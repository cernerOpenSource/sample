#!/usr/bin/env python
import csv
from collections import defaultdict
with open('userrev.csv', 'rb') as newf:
    new_reader = csv.reader(newf)
    
    for row in new_reader:
        x=row[0]
        reader = csv.reader(newf)
        for col in reader:
            if x==col[0]:
                print col[1]
        
newf.close()

    
       
        

