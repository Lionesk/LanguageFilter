# input: a context file
# output: a dictionary
import re

# input: a filename and the string representing the word being searched for
# output: a dictionary containing frequencies for each word in the token's context (max. 14 words on either side, but varies by line)
def wordbag(f,s):
	size = 0
	n = 3
	raw = open(f, 'r')
	raw2 = raw.readlines()
	freqs = {}
	for ln in range(len(raw2)):
		raw2[ln] = raw2[ln].replace('\n','')
		raw2[ln] = raw2[ln].split()
	#print raw2
	for ln in raw2:
		for w in ln:
			freqs[w] = 0.0 # initializes frequency
	for ln in range(len(raw2)):
		for w in range(len(raw2[ln])):
			if raw2[ln][w] == s:
				start = max(w-n,0)
				stop = min(w+n+1,len(raw2[ln]))
				immcont = []
				for i in range(start,stop):
					immcont.append(raw2[ln][i])	
				# print immcont
				for t in immcont:
					freqs[t] = freqs[t] + 1
	
	# print freqs
	return freqs

# input: a word to disambiguate
# output: a list of ratios. Higher -> more likely to be found in clean context
def getRatios(s):
	f0 = 'wsd/' + s + '-0.txt'
	f1 = 'wsd/' + s + '-1.txt'
	c0 =  wordbag(f0,s)
	c1 =  wordbag(f1,s)

	for k in c0:
		if k not in c1:
			c1[k] = 0.0
	for k in c1:
		if k not in c0:
			c0[k] = 0.0
	for k in c0:
		c0[k] = c0[k] + 0.1
	for k in c1:
		c1[k] = c1[k] + 0.1
#	print c0
	probs0 = {}
	probs1 = {}
	size0 = 0.0
	size1 = 0.0
	for k in c0:
		size0 = size0 + c0[k]
	for k in c1:
		size1 = size1 + c1[k]
	for k in c0:
		probs0[k] = float(c0[k])/float(size0)
	for k in c1:
		probs1[k] = float(c1[k])/float(size1)
	# print probs0
	# print probs1
	ratios = {}
	for k in c0:
		ratios[k] = probs0[k]/probs1[k]
	# printTop10(ratios) # if you want
	# print ratios
	return ratios

def printTop10(ratios): # for research and fun, shouldn't be called from main.py
	rlist = []
	for k in ratios:
		rlist.append([ratios[k],k])
	rlist = sorted(rlist)
	print 'MOST LIKELY TO BE FOUND IN PROFANE CONTEXT'
	for n in range(10):
		print rlist[n][1]
	print '...'
	print 'MOST LIKELY TO BE FOUND IN CLEAN CONTEXT:'
	for n in range(len(rlist)-10, len(rlist)):
		print rlist[n][1]

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
			# print r[w]
			product = product * r[w]
			# print w
			# print product
	if product > 1:
		return False
	return True

# carlin = open('carlin.txt','r')
# carlin2 = carlin.read().replace('\n',' ')
# print assignWeights(carlin2.split(),getRatios('chink'))