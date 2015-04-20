##this file contains all the fucntions for removing/replacing profane words from a text
##that is, all words that are unambiguously profane -- which are contained in the profaneWords plain text file

##is passed a line from the main function and finds the words that are on the profane word list
def compare(x):
<<<<<<< HEAD
    wordList = open('profaneWords.txt', 'r')
    for w in wordList.readline():
        if x.lower() == w:
=======
    wordListRaw = open('profaneWords.txt', 'r')
    wordListRaw2 = wordListRaw.readlines()
    wordList = []
    for line in range(len(wordListRaw2)):
    	wordList.append(wordListRaw2[line].split('\t')) # splits TSV
    for w in range(1,len(wordList)): # ignores headers
        if x == wordList[w][0]: # looks only at first 'column'
>>>>>>> d3b035fb228291c607af700ca92b19a4178498fc
            return True
    return False
# print compare('fuck') # for debugging
# print compare('sex')
# print compare('word')
