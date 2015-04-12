##this file contains all the fucntions for removing/replacing profane words from a text
##that is, all words that are unambiguously profane -- which are contained in the profaneWords plain text file

##is passed a line from the main function and finds the words that are on the profane word list
wordlist = open(profaneWords, r)

def compare(str x):
    for w in wordlist.readline():
        if x == w:
            return True
    return False

def censor(str x):
    out = ''
    for c in x:
        out+=*
    return out
