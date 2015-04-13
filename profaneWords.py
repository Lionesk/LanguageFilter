##this file contains all the fucntions for removing/replacing profane words from a text
##that is, all words that are unambiguously profane -- which are contained in the profaneWords plain text file

##is passed a line from the main function and finds the words that are on the profane word list
wordlist = open(profaneWords.txt, r)

def compare(str):
    for w in wordlist.readline():
        if str == w:
            return True
    return False

def censor(str):
    out = ''
    for c in str:
        out+='*'
    return out
