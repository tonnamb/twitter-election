import sqlite3 as lite
import sys
from collections import Counter
from itertools import chain
import re


con = lite.connect('clinton1.db')

with con:    
    
    cur = con.cursor()
    con.text_factory = str
    cur.execute("SELECT tweet FROM Clinton")

    rows = cur.fetchall() # Retrieve all records

    w_list = []
    for sr in list(chain(*rows)):
    	w_list.extend(w.lower() for w in re.findall(r'\w+', sr))

    cnt = Counter(w_list)
    w_name = cnt.keys()
    w_count = cnt.values()
    for i in reversed(cnt.most_common()):
    	print i