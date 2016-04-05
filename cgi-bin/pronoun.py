import csv
import collections
import sqlite3
import nltk
file = open("userrev.csv","rb")
c = csv.reader(file)
unor=[]
for row in c:
    unor.append(row[0])
b=set(unor)
print b
file.close()
file = open("userrev.csv","rb")
c2 = csv.reader(file)
con = sqlite3.connect("PROJECT")
cursor = con.cursor()
for a in b:
    for row in c2:
        if str(a)==str(row[0]):
            
            tagged_sent = nltk.pos_tag(row[6].split())
            
            personalpronoun=[word for word, pos in tagged_sent if pos == 'PRP']
            status="no"
            for i in personalpronoun:
                count=0
                c=0
                if i.lower()=='i' or i.lower()=='me' or i.lower()=='myself' or i.lower=='we' or i.lower()=='our' or i.lower()=='ourself':
                    count=count+1
                else:
                    c=c+1
                
                if c>count:
                    status="yes"    
                
                    
            print row[0],status
            cursor = con.execute("SELECT uid,status from feature3pronoun where uid=?",(row[0],))
            if cursor.fetchone():
                cursor.execute("UPDATE feature3pronoun SET status=? WHERE uid=?", (status, row[0]))
            else:
                cursor.execute("insert into feature3pronoun \
                    values(?,?)",(row[0],status))
            con.commit()
    file.close()
    file = open("userrev.csv","rb")
    c2 = csv.reader(file)
            
file.close()
        
