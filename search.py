# Search for hashtags and author's screen name

import tweepy
import limhan

consumer_key = 'bfoN8IIW5YUN5tKD7vRaJJ5aY'
consumer_secret = 'pZw1UCPbjDQjrTp01IgZL36h4JOo3U0GrokaRUNMHVUVRY6yiq'
access_token = '1349515753-oGbkzRBurZRAO5AopHY2ZZDbWEtWfeGjqOs6G3X'
access_token_secret = 'fmXsNFxwF3vQYSdlofPzIUafdCtAQ2yex0rW96HAbsHoh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

query = '#ImWithHer'
max_tweets = 3
searched_tweets = [status for status in \
	limhan.limit_handled(tweepy.Cursor(api.search, q=query).items(max_tweets))]

for tw in searched_tweets:
	print tw.text
	print tw.author.screen_name