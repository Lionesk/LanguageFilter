##this file contains all the fucntions for removing/replacing profane words from a text
##that is, all words that are unambiguously profane -- which are contained in the profaneWords plain text file
import re
from levenshtein import levenshtein
import wsd

#input: x, a string passed from main.py; c, the string's context (n words in either direction, including x, list format)
#output: True if word should be censored, False otherwise
def compare(y, con):
	x = y.lower()
	c = []
	for w in range(len(con)):
		c.append(con[w][0].lower())
		c[w] = c[w][0].replace('\n','')
		c[w] = re.sub(r'[^a-z ]','',c[w][0])
	x = x.replace('\n','')
	x = re.sub(r'[^a-z ]','',x)
	wordListRaw = open('profaneWords.txt', 'r')
	wordListRaw2 = wordListRaw.readlines()
	wordList = []
	for line in range(len(wordListRaw2)):
		wordList.append(wordListRaw2[line].split('\t')) # splits TSV
	for w in range(1,len(wordList)): # ignores headers
		if (wordList[w][0] == x or wordList[w][0] + 's' == x or wordList[w][0] + 'es' == x or wordList[w][0] + 'ed' == x) and wordList[w][2] == '0':
			return True # avoids excess bureaucracy if not needed 
		if wordList[w][0] in x: # looks only at first 'column'	
			if wordList[w][1] == '0' and wordList[w][2] == '0': # i.e. if no ambiguity possible
			#	print x + ' unambiguous'
				return True
			elif wordList[w][1] == '1': # if word is semantically ambiguous in a restricted context (non-profane only in fossilized expressions)
			#	print x + ' semantically ambiguous, restricted context'
				return examineImmediateContext(x, c)
			elif wordList[w][1] == '2': # if word is always semantically ambiguous
			#	print x + ' semantically ambiguous, unrestricted context'
				return wsd.assignWeights(c, wsd.getRatios(wordList[w][0]))
			elif wordList[w][2] == '1': # if word is string ambiguous
			#	print x + ' string ambiguous'
				return stringCheck(x)			
	# print 'no objection found to ' + x + ', returning false'
	return False

# input: a string passed from compare(x)
# output: True if word should be censored, False otherwise
def examineImmediateContext(x, c):
	return True

#INPUT: A string passed from the compare function.
#OUTPUT: A boolean, whether or not the word is found in the whitelist.
def stringCheck(x):
	whitelistRaw = open('whitelist.csv','r')
	whitelist = whitelistRaw.readlines()
	for w in range(len(whitelist)):
		whitelist[w] = whitelist[w].replace('\n','')
	for w in whitelist:
		if levenshtein(w, x) <= 1 and len(x) >= 6: # allows for minor misspellings of innocuous word, but only in longer words
			# print 'variant of ' + w
			return False
	return True
