# get all posts of a user

import tweepy

consumer_key = 'bfoN8IIW5YUN5tKD7vRaJJ5aY'
consumer_secret = 'pZw1UCPbjDQjrTp01IgZL36h4JOo3U0GrokaRUNMHVUVRY6yiq'
access_token = '1349515753-oGbkzRBurZRAO5AopHY2ZZDbWEtWfeGjqOs6G3X'
access_token_secret = 'fmXsNFxwF3vQYSdlofPzIUafdCtAQ2yex0rW96HAbsHoh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('sarahhhkidder')

print user.screen_name
print user.followers_count
#for friend in user.friends():
#	print friend.screen_name
posts = api.user_timeline('sarahhhkidder')

i = 1
for post in posts:
	print '{0}: '.format(i) + post.text
	i = i + 1