import csv
import collections
import sqlite3
import re
file = open("userrev.csv","rb")
#f2 = file('pro.csv', 'rb')
#f3 = file('om.csv', 'wb')
#for col in c1:
        #print row
        #if row==col[0]:
            #print col[1]
f1=open("pro.csv")
c=csv.reader(f1)
q=0
f=0
c1 = csv.reader(file)
unor=[]
for row in c1:
    unor.append(row[0])
b=set(unor)
file.close()
file = open("userrev.csv")
c2 = csv.reader(file)
l=[]
con = sqlite3.connect("PROJECT")
cur = con.cursor()
for a in b:
    print a,
    for row1 in c2:
        if str(a)==str(row1[0]):
            print row1[1],
            for row2 in c:
                if str(row1[1])==str(row2[0]):
                    print row2[5],
                    #x1=row2.split(',')
                    #y1=row1.split(',')
                    #row2 = row2.replace('"', '').strip()
                    #x1,x2,x3,x4,x5 = map(int, row2.split())
                    #row1 = row1.replace('"', '').strip()
                    #y1,y2,y3,y4,y5,y6,y7,y8 = map(int, row1.split())
                    
                    x1=int(float(row2[5]))
                    x2=int(float(row1[4]))
                    if x1==0:
                        x1=3.5
                    star=x2/x1*100
                    if star<=50:
                        stat="yes"
                    else:
                        stat="no"
                    print stat
                    l.append(stat)    
                
                    break
                    
                    
            f1.close()
            f1=open("pro.csv")
            c=csv.reader(f1)
    for i in l:
        print i
        if str(i)==str("yes"):
            q=q+1
        f=f+1
    l=[]
    print q,f
    if q>=f:
        status="yes"
    else:
        status="no"
    q=0
    f=0
    print a,status
    cur.execute("insert into feature2stars \
            values(?,?)",(a,status))
    con.commit()
    print "\n"
    file.close()
    file = open("userrev.csv")
    c2 = csv.reader(file)
            
file.close()

            
