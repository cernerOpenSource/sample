#!/usr/bin/env python
import sqlite3
con = sqlite3.connect("PROJECT")
cur = con.cursor()
uname="sap"
pwd="fddf"
cursor = con.execute("SELECT username, pwd from userdata where username=? and pwd=?",(uname,pwd,))
if cursor.fetchone():
    print("Found!")

else:
    print("Not found...")


    