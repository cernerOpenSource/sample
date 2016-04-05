import csv
import collections
import sqlite3
import nltk
file = open("userrev.csv","rb")
c = csv.reader(file)
con = sqlite3.connect("PROJECT")
cursor = con.cursor()
for row in c:
    
    tagged_sent = nltk.pos_tag(row[6].split())
    
    personalpronoun=[word for word, pos in tagged_sent if pos == 'PRP']
    for i in personalpronoun:
        count=0
        c=0
        if i.lower()=='i' or i.lower()=='me' or i.lower()=='myself' or i.lower=='we' or i.lower()=='our' or i.lower()=='ourself':
            count=count+1
        else:
            c=c+1
        if c>count:
            status="yes"    
        else:
            status="no"
        cursor = con.execute("SELECT uid,status from feature3pronoun where uid=?",(row[1],))
        if cursor.fetchone():
            cursor.execute("UPDATE feature3pronoun SET status=? WHERE uid=?", (status, row[1]))
        else:
            cursor.execute("insert into feature3pronoun \
            values(?,?)",(row[1],status))
        con.commit()
            
file.close()
        
