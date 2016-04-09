import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con: # More compact code using with, provides automatic error handling

	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()') # Execute SQL Statement

	data = cur.fetchone() # Retrive one record

	print "SQLite version: %s" % data