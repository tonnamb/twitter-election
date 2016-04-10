import tweepy
import f_mine
import sqlite3 as lite
import sys

consumer_key = 'bfoN8IIW5YUN5tKD7vRaJJ5aY'
consumer_secret = 'pZw1UCPbjDQjrTp01IgZL36h4JOo3U0GrokaRUNMHVUVRY6yiq'
access_token = '1349515753-oGbkzRBurZRAO5AopHY2ZZDbWEtWfeGjqOs6G3X'
access_token_secret = 'fmXsNFxwF3vQYSdlofPzIUafdCtAQ2yex0rW96HAbsHoh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

max_tweets = 1000
searched_tweets = f_mine.mine(api, '#hillarymostqualified', max_tweets)
print len(searched_tweets)

format_sql = []
for tw in searched_tweets:
	format_sql.append((tw.author.screen_name, ' '.join(tw.text.splitlines())))

con = lite.connect('clinton3.db')

with con:

	cur = con.cursor()

	cur.execute("DROP TABLE IF EXISTS Clinton")
	cur.execute("CREATE TABLE Clinton( \
		Id INTEGER PRIMARY KEY, \
		screen_name TEXT, \
		tweet TEXT, \
		UNIQUE(screen_name))")
	cur.executemany("INSERT OR IGNORE INTO Clinton(screen_name, tweet) VALUES(?, ?)", format_sql) # Execute many statements

#for tw in searched_tweets:
#	print '{0} ({1}): '.format(tw.author.screen_name, tw.author.location) \
#		+ ' '.join(tw.text.splitlines())