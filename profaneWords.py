##this file contains all the fucntions for removing/replacing profane words from a text
##that is, all words that are unambiguously profane -- which are contained in the profaneWords plain text file
import re
import levenshtein
import wsd
##is passed a line from the main function and finds the words that are on the profane word list
# input: x, a string passed from main.py; c, the string's context (10 words in either direction, including x)
# output: True if word should be censored, False otherwise
def compare(y, con):
	x = y.lower()
	c = []
	for w in range(len(con)):
		c.append(con[w][0].lower())
		c[w] = c[w][0].replace('\n','')
		c[w] = re.sub(r'[^a-z ]','',c[w][0])
	x = x.replace('\n','')
	# print x
	# print c
	x = re.sub(r'[^a-z ]','',x)
	wordListRaw = open('profaneWords.txt', 'r')
	wordListRaw2 = wordListRaw.readlines()
	wordList = []
	for line in range(len(wordListRaw2)):
		wordList.append(wordListRaw2[line].split('\t')) # splits TSV
	for w in range(1,len(wordList)): # ignores headers
		if wordList[w][0] in x: # looks only at first 'column'	
			if wordList[w][1] == '0' and wordList[w][2] == '0': # i.e. if no ambiguity possible
				# print x + ' unambiguous'
				return True
			elif wordList[w][2] == '1':
				# print x + ' string ambiguous'
				return stringCheck(x)
			elif wordList[w][1] == '1':
				# print x + ' semantically ambiguous, restricted context'
				return examineImmediateContext(x, c)
			elif wordList[w][1] == '2':
				# print x + ' semantically ambiguous, unrestricted context'
				return wsd.assignWeights(c, wsd.getRatios(wordList[w][0]))
	# print 'no objection found to ' + x + ', returning false'
	return False

# input: a string passed from compare(x)
# output: True if word should be censored, False otherwise

def examineImmediateContext(x, c):
	return True

def stringCheck(x):
	whitelistRaw = open('emwClean.csv','r')
	whitelist = whitelistRaw.readlines()
	white = ''.join(whitelist)
	exact = '\n'+x+'\n'
	# print white
	if exact in white:
		return False
	else:
		return True