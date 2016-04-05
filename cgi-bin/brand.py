#!/usr/bin/env python
import csv
file = open("newdata.csv")
reader = csv.reader(file)
fo=open("brandcheck.txt","a+")
for line in reader:
    fo.write(line[1])
fo.close()
            

    
       
        

