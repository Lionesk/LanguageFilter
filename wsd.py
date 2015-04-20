# input: a context file
# output: a dictionary
import re

def wordbag(f,s):
	raw = open(f, 'r')
	raw2 = raw.readlines()
	freqs = {}
	for ln in range(len(raw2)):
		raw2[ln] = raw2[ln].replace('\n','')
		raw2[ln] = raw2[ln].split()
	for l in raw2:
		for w in l:
			freqs[w] = 0
	for l in raw2:
		for w in l:
			freqs[w] = freqs[w] + 1
	for f in freqs:
		freqs[f] = freqs[f] + 0.1
	return freqs

# input: a word to disambiguate
# output: a list of ratios. Higher -> more likely to be found in clean context
def getRatios(s):
	f0 = 'wsd/' + s + '-0.txt'
	f1 = 'wsd/' + s + '-1.txt'
	c0 =  wordbag(f0,s)
	c1 =  wordbag(f1,s)
#	print c0
#	print c1
	for k in c0:
		if k not in c1:
			c1[k] = 0.1
	for k in c1:
		if c1[k] != 0.1 and k not in c0:
			c0[k] = 0.1
	ratios = {}
#	rlist = []
	for k in c0:
		ratios[k] = float(c0[k])/float(c1[k])
#		rlist.append([ratios[k], k])
#	rlist = sorted(rlist)
#	print 'MOST LIKELY TO BE FOUND IN PROFANE CONTEXT'
#	for n in range(10):
#		print rlist[n][1]
#	print '...'
#	print 'MOST LIKELY TO BE FOUND IN CLEAN CONTEXT:'
#	for n in range(len(rlist)-10, len(rlist)):
#		print rlist[n][1]
	return ratios

# input: a list consisting of a sentence, and a dictionary (the output of getRatios(s))
# output: True if product < 1 (i.e. word ) 
def assignWeights(cont, r):
	for s in cont: 
		s = s.lower()
		s = re.sub(r'[^a-z ]','',s)
		# print s
	product = 1.0
	# print cont
	for w in cont:
		if w in r:
			product = product * r[w]
			# print w
			# print product
	if product > 1:
		return False
	return True

#carlin = open('carlin.txt','r')
#carlin2 = carlin.read().replace('\n',' ')
#print assignWeights(carlin2.split(),getRatios('balls'))