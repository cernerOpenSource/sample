import csv
import collections
file = open("userrev.csv","rb")
#f2 = file('pro.csv', 'rb')
#f3 = file('om.csv', 'wb')
#for col in c1:
        #print row
        #if row==col[0]:
            #print col[1]
f1=open("pro.csv")
c=csv.reader(f1)

c1 = csv.reader(file)
unor=[]
for row in c1:
    unor.append(row[0])
b=set(unor)
file.close()
file = open("userrev.csv")
c2 = csv.reader(file)
ofile  = open('ttest.csv', "wb")
writer = csv.writer(ofile)
l=[]
import sqlite3
con = sqlite3.connect("PROJECT")
cur = con.cursor()
for a in b:
    print a,
    for row1 in c2:
        if str(a)==str(row1[0]):
            print row1[1],
            for row2 in c:
                if str(row1[1])==str(row2[0]):
                    print row2[2],
                    l.append(row2[2])
                    break
            f1.close()
            f1=open("pro.csv")
            
            c=csv.reader(f1)
    new=collections.Counter(l)
    length=len(l)
    
    m=new.values()
    print m
    for d in m:
            z=(d/length)*100
            
            if z>=20:
                status="yes"
            else:
                status="no"
    cur.execute("insert into feature1brand \
        values(?,?)",(a,status))
    con.commit()
    l=[]
    print "\n"
    file.close()
    file = open("userrev.csv")
    c2 = csv.reader(file)
            
file.close()

            
