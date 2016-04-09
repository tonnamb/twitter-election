import tweepy
import limhan

def mine(api, query, max_tweets):
	searched_tweets = [status for status in \
	limhan.limit_handled(tweepy.Cursor(api.search, q=query).items(max_tweets))]
	return searched_tweets