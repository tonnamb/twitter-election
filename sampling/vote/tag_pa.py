import csv
with open('pa.csv') as csvfile:
	rows = csv.reader(csvfile)
	rows = list(rows)

import tweepy
import time
import numpy as np

consumer_key = 'bfoN8IIW5YUN5tKD7vRaJJ5aY'
consumer_secret = 'pZw1UCPbjDQjrTp01IgZL36h4JOo3U0GrokaRUNMHVUVRY6yiq'
access_token = '1349515753-oGbkzRBurZRAO5AopHY2ZZDbWEtWfeGjqOs6G3X'
access_token_secret = 'fmXsNFxwF3vQYSdlofPzIUafdCtAQ2yex0rW96HAbsHoh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

from collections import Counter
import re

v_matrix = []
for row in rows[:100]:
	user_name = row[0]
	try:
		posts = api.user_timeline(user_name)
	except tweepy.RateLimitError:
            time.sleep(15 * 60)
	w_list = []
	for post in posts:
		w_list.extend(w.lower() for w in re.findall(r'\w+', post.text))
	cnt = Counter(w_list)
	w_name = cnt.keys()
	w_count = cnt.values()
	v_matrix.append([cnt['imwithher'],cnt['hillyes'],cnt['hillarymostqualified'],cnt['votehillary'], \
		cnt['feelingthebern'],cnt['berniestrong'],cnt['bernieorbust'],cnt['votebernie'], \
		cnt['trumparmy'],cnt['makeamericagreatagain'],cnt['trumptrain'],cnt['votetrump'], \
		cnt['unitewithcruz'],cnt['cruzcrew'],cnt['choosecruz'],cnt['votecruz']])

	print cnt.most_common(20)
	print 'imwithher: {0}'.format(cnt['imwithher'])
	print 'hillyes: {0}'.format(cnt['hillyes'])
	print 'hillarymostqualified: {0}'.format(cnt['hillarymostqualified'])
	print 'votehillary: {0}'.format(cnt['votehillary'])
	print 'feelingthebern: {0}'.format(cnt['feelingthebern'])
	print 'berniestrong: {0}'.format(cnt['berniestrong'])
	print 'bernieorbust: {0}'.format(cnt['bernieorbust'])
	print 'votebernie: {0}'.format(cnt['votebernie'])
	print 'trumparmy: {0}'.format(cnt['trumparmy'])
	print 'makeamericagreatagain: {0}'.format(cnt['makeamericagreatagain'])
	print 'trumptrain: {0}'.format(cnt['trumptrain'])
	print 'votetrump: {0}'.format(cnt['votetrump'])
	print 'unitewithcruz: {0}'.format(cnt['unitewithcruz'])
	print 'cruzcrew: {0}'.format(cnt['cruzcrew'])
	print 'choosecruz: {0}'.format(cnt['choosecruz'])
	print 'votecruz: {0}'.format(cnt['votecruz'])
	print np.sum(v_matrix)



print v_matrix
print np.sum(v_matrix)