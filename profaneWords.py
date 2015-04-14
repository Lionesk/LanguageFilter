##this file contains all the fucntions for removing/replacing profane words from a text
##that is, all words that are unambiguously profane -- which are contained in the profaneWords plain text file

##is passed a line from the main function and finds the words that are on the profane word list
def compare(x):
    wordList = open('profaneWords.txt', 'r')
    for w in wordList.readline():
        if x.lower() == w:
            return True
    wordList.close()
    return False
