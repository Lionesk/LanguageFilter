##this file contains all the fucntions for removing/replacing profane words from a text
##that is, all words that are unambiguously profane -- which are contained in the profaneWords plain text file
import re
##is passed a line from the main function and finds the words that are on the profane word list
def compare(x):
	x = x.lower()
	wordListRaw = open('profaneWords.txt', 'r')
	wordListRaw2 = wordListRaw.readlines()
	wordList = []
	for line in range(len(wordListRaw2)):
		wordList.append(wordListRaw2[line].split('\t')) # splits TSV
	for w in range(1,len(wordList)): # ignores headers
		if wordList[w][0] in x: # looks only at first 'column'
			checkVariations(x)
			return True
	return False

def checkVariations(x):
	pass
# print compare('fuck') # for debugging
# print compare ('Fuck')
# print compare('fucks')
# print compare('word')
# print compare('sex')
# print compare('word')
