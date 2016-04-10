import csv
with open('hi.csv') as csvfile:
	rows = csv.reader(csvfile)
	rows = list(rows)

import numpy as np
import re
from collections import Counter

v_matrix = []
v_result = []
template = [[1, 0, 0, 0], [0, 1, 0 ,0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
for row in rows:
	tw = row[1]
	w_list = []
	w_list.extend(w.lower() for w in re.findall(r'\w+', tw))
	cnt = Counter(w_list)
	w_name = cnt.keys()
	w_count = cnt.values()
	v_vector = [cnt['imwithher']+cnt['hillyes']+cnt['hillarymostqualified']+cnt['votehillary'], \
		cnt['feelingthebern']+cnt['berniestrong']+cnt['bernieorbust']+cnt['votebernie'], \
		cnt['trumparmy']+cnt['makeamericagreatagain']+cnt['trumptrain']+cnt['votetrump'], \
		cnt['unitewithcruz']+cnt['cruzcrew']+cnt['choosecruz']+cnt['votecruz']]
	v_matrix.append(v_vector)
	winner = np.argwhere(v_vector == np.amax(v_vector))
	if len(winner)==1:
		v_max = np.argmax(v_vector)
	else:
		v_max = 4
	v_result.append(template[v_max])

	#print cnt.most_common(20)
	#print 'imwithher: {0}'.format(cnt['imwithher'])
	#print 'hillyes: {0}'.format(cnt['hillyes'])
	#print 'hillarymostqualified: {0}'.format(cnt['hillarymostqualified'])
	#print 'votehillary: {0}'.format(cnt['votehillary'])
	#print 'feelingthebern: {0}'.format(cnt['feelingthebern'])
	#print 'berniestrong: {0}'.format(cnt['berniestrong'])
	#print 'bernieorbust: {0}'.format(cnt['bernieorbust'])
	#print 'votebernie: {0}'.format(cnt['votebernie'])
	#print 'trumparmy: {0}'.format(cnt['trumparmy'])
	#print 'makeamericagreatagain: {0}'.format(cnt['makeamericagreatagain'])
	#print 'trumptrain: {0}'.format(cnt['trumptrain'])
	#print 'votetrump: {0}'.format(cnt['votetrump'])
	#print 'unitewithcruz: {0}'.format(cnt['unitewithcruz'])
	#print 'cruzcrew: {0}'.format(cnt['cruzcrew'])
	#print 'choosecruz: {0}'.format(cnt['choosecruz'])
	#print 'votecruz: {0}'.format(cnt['votecruz'])
	#print np.sum(v_matrix)

#print v_matrix
#print np.sum(v_matrix)

np.savetxt(
    'results.csv',           # file name
    v_matrix,                # array to save
    fmt='%i',
    delimiter=',',          # column delimiter
    newline='\n',           # new line character
    footer='end of file',   # file footer
    comments='# ',          # character to use for comments
    header='Clinton, Bernie, Trump, Cruz')      # file header

print np.sum(v_result, axis=0)