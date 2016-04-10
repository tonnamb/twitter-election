import sqlite3 as lite
import sys


con = lite.connect('clinton.db')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT tweet FROM Clinton")

    rows = cur.fetchall() # Retrieve all records

    print rows[0]