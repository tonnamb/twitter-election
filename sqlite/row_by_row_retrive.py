import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Cars") # SQL statement does not change

    while True:
      
        row = cur.fetchone() # Fetch row by row
        
        if row == None: # Loop is terminated when we read the last row
            break
            
        print row[0], row[1], row[2]