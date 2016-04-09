import sqlite3 as lite
import sys

con = None

try:
	con = lite.connect('test.db')

	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()') # Execute the SQL statement

	data = cur.fetchone() # Fetch one record, since we retrieved only one record

	print "SQLite version: %s" % data

except lite.Error, e:

	print "Error %s:" % e.args[0]
	sys.exit(1)

finally:

	if con:
		con.close()