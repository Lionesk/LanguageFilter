# this file contains all the fucntions for removing/replacing profane words from a text
# that is, all words that are unambiguously profane -- which are contained in the profaneWords plain text file
import re
from levenshtein import levenshtein
import wsd


# input x, a string passed from main.py; c, the string's context (n words in either direction, including x, list format)
# output: True if word should be censored, False otherwise
def compare(y, con):
    x = y.lower()
    c = []
    for w in range(len(con)):
        c.append(con[w][0].lower())
        c[w] = c[w].replace('\n', '')
        c[w] = re.sub(r'[^a-z ]', '', c[w])  # strips all non-alphanumeric characters
    x = x.replace('\n', '')  # strips newline
    x = re.sub(r'[^a-z ]', '', x)  # turns to lowercase, strips all non-alphanumeric characters
    # print c
    wordListRaw = open('profaneWords.txt', 'r')  # opens the blacklist
    wordListRaw2 = wordListRaw.readlines()
    wordList = []
    for line in range(len(wordListRaw2)):
        wordList.append(wordListRaw2[line].split('\t'))  # splits TSV
    for w in range(1, len(wordList)):  # ignores headers
        if (wordList[w][0] == x and wordList[w][1] == '0') or (
                                wordList[w][0] + 's' == x or wordList[w][0] + 'es' == x or wordList[w][0] + 'ed' == x):
            return True  # avoids excess bureaucracy if not needed
        if wordList[w][0] in x:  # looks only at first 'column'
            censor = True  # default value
            if wordList[w][1] == '0' and wordList[w][2] == '0':  # i.e. if no ambiguity possible
                return censor
            if wordList[w][1] == '1':
                # if word is semantically ambiguous in a restricted context (non-profane only in fossilized expressions)
                if examineImmediateContext(x, c):  # if word is not in an exceptional context
                    return stringCheck(x)  # make sure it's not an accidental string and return that
                else:
                    return examineImmediateContext(x, c)
            if wordList[w][1] == '2':  # if word is always semantically ambiguous
                censor = wsd.assignWeights(c, wsd.getRatios(wordList[w][0]))  # use NB classifier (see wsd.py)
            elif wordList[w][2] == '1':  # if word is string ambiguous
                censor = stringCheck(x)
            return censor
        if levenshtein(wordList[w][0], x) <= 1:  # if word is less than 1 letter away from a word on the blacklist
            if isWord(x) == False:  # check to see if it's a real word in the full dictionary
                return False
            else:
                return True
    return False


# input: a string passed from compare(x) and its context
# output: True if word should be censored, False otherwise
def examineImmediateContext(x, c):
    wordListRaw = open('profaneWords.txt', 'r')
    wordListRaw2 = wordListRaw.readlines()
    wordList = []
    for line in range(len(wordListRaw2)):
        wordList.append(wordListRaw2[line].split('\t'))  # splits TSV
    cens = True
    for w in range(1, len(wordList)):
        if wordList[w][0] in x:
            for n in c:
                if wordList[w][3] in n:
                    # if the word that makes it acceptable is in the context (at all, either direction)
                    cens = False
    return cens


def isWord(x):  # sees if word is in emwClean.csv
    words = open('emwClean.csv', 'r')
    wordlist = words.readlines()
    for w in wordlist:
        if w in x:
            return True
        else:
            return False


def stringCheck(x):
    # sees if word is in truncated whitelist (shortened from emwClean.csv for speed of operation, to contain only
    # clean words with coincidental profanity)
    # INPUT: A string passed from the compare function.
    # OUTPUT: A boolean, whether or not the word is found in the whitelist.
    whitelistRaw = open('whitelist.csv', 'r')
    whitelist = whitelistRaw.readlines()
    for w in range(len(whitelist)):
        whitelist[w] = whitelist[w].replace('\n', '')
    for w in whitelist:
        if w == x or (levenshtein(w, x) <= 1 and len(x) >= 6) or (x == (w + 's')) or (x == (w + 'es')) or (x == (
                    w + 'ed')):
            # allows for minor misspellings of innocuous word, but only in longer words; also allows plurals
            # and past tense
            # print w
            return False  # i.e. don't censor
    return True  # i.e. censor (default value)
