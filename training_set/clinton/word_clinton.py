import sqlite3 as lite
import sys
from collections import Counter


con = lite.connect('clinton.db')

with con:    
    
    cur = con.cursor()
    con.text_factory = str
    cur.execute("SELECT tweet FROM Clinton")

    rows = cur.fetchall() # Retrieve all records

    cnt = Counter(rows[0][0].split())
    print cnt.keys()
    print cnt.values()
    # for i in rows[0][0].split():
    #	print i
    # counter = Counter(rows[0][0].split)
    # w_key = counter.keys()
    # w_count = counter.values()