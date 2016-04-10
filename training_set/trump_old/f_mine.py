import tweepy
import f_limhan

def mine(api, query, max_tweets):
	searched_tweets = [status for status in \
	f_limhan.limit_handled(tweepy.Cursor(api.search, q=query).items(max_tweets))]
	return searched_tweets