#!/usr/bin/env python
import csv
from collections import defaultdict
#file = open("newdata.csv")
#reader = csv.reader(file)
#for line in reader:
    #print line[1]
#file.close()
fo=open('om1.csv','a')
with open('newdata.csv', 'rb') as newf:
    new_reader = csv.reader(newf)
    reader = csv.reader(newf)
    for row in new_reader:
        x=row[0]
        for col in reader:
            if x==col[0]:
                fo.write(col[1])
                fo.write('\n')
            else:
                fo.write("new user")
                break

        
newf.close()
fo.close()
    
       
        

