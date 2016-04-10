import sqlite3 as lite
import sys

con = lite.connect(':memory:') # Create in memory

with con:

	cur = con.cursor()
	cur.execute("CREATE TABLE Friends( Id INTEGER PRIMARY KEY, Name TEXT);")
	# PRIMARY KEY automatically generate Id
	cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
	# INSERT INTO Friends(Name)
	cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
	cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
	cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")

	lid = cur.lastrowid
	print "The last Id of the inserted row is %d" % lid