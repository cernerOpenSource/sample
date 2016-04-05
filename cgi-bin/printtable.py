#!/usr/bin/env python
import sqlite3
conn = sqlite3.connect('PROJECT')
print "Opened database successfully";

cursor = conn.execute("SELECT uid,status  from feature1brand")
i=0
for row in cursor:
   print "ID = ", row[0]
   print "STATUS = ", row[1]
   i=i+1
   
print i
print "Operation done successfully";
conn.close()