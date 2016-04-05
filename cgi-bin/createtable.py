#!/usr/bin/env python

import sqlite3

con = sqlite3.connect("PROJECT")
cur = con.cursor()
cur.execute('''CREATE TABLE final(
                  uid  TEXT PRIMARY KEY,
                  weight INT
                )''')
con.close()
