##this file contains all the fucntions for removing/replacing profane words from a text
##that is, all words that are unambiguously profane -- which are contained in the profaneWords plain text file
import re
import levenshtein
import wsd
import emw.csv as emw
##is passed a line from the main function and finds the words that are on the profane word list
# input: x, a string passed from main.py; c, the string's context (10 words in either direction, including x)
# output: True if word should be censored, False otherwise
def compare(x, c):
	x = x.lower()
	c = c.lower()
	x = x.replace('\n','')
	c = c.replace('\n','')
	print x
	print c
	x = re.sub(r'[^a-z ]','',x)
	c = re.sub(r'[^a-z ]','',c)
	wordListRaw = open('profaneWords.txt', 'r')
	wordListRaw2 = wordListRaw.readlines()
	wordList = []
	for line in range(len(wordListRaw2)):
		wordList.append(wordListRaw2[line].split('\t')) # splits TSV
	for w in range(1,len(wordList)): # ignores headers
		if wordList[w][0] in x: # looks only at first 'column'
			if wordList[w][1] == 0 and wordList[w][2] == 0: # i.e. if no ambiguity possible
				return True
			if wordList[w][1] == 1:
				return examineImmediateContext(x, c)
			if wordList[w][1] == 2:
				return wsd.
		else:
			if checkVariations = True:
				return True
	return False

# input: a string passed from compare(x)
# output: True if word should be censored, False otherwise
def examineImmediateContext(x, c):
	return True
# print compare('fuck') # for debugging
# print compare ('Fuck')
# print compare('fucks')
# print compare('word')
# print compare('sex')
# print compare('word')
