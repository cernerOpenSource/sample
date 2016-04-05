#!/usr/bin/env python
import sqlite3
con = sqlite3.connect("PROJECT3")
cur = con.cursor()
cursor = con.execute("SELECT username, pwd from userdata")
for row in cursor:
    print "ID = ", row[0]
    print "PASSWORD = ", row[1]
con.close()
