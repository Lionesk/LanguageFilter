import sys, os
import profaneWords, variations

##adding functionality for reading the profanity from files, making them into things that can be passed to functions in this
##or other modules
def fileToLines(filename):
    openedFile = open(filename, 'r')
    lines = openedFile.read().splitlines()
    openedFile.close()
    return lines

##making a function to turn a text based input from web into lines to pass to functions
def stringToLines(string):
    lines = string.splitlines()
    return lines

def linesToList(lines):
    output = []
    for l in lines:
        for w in l.split():
            output.append(w)
    output2 = [[] for s in range(len(output))]
    for s in range(len(output)):
        output2[s].append(output[s]) # makes into list of lists format
    return output2

def asterisk(s): 
# INPUT: a string. OUTPUT: that string, with all characters except the first replaced with asterisks
    if len(s) < 3:
        return s
    cens = ''
    cens = cens + s[0]
    for n in range(len(s)-2):
        cens = cens + '*'
    cens = cens + s[len(s)-1]
    return cens

def censor(words): 
# INPUT: a list of lists. For each sublist, words[n][0] is a word, and words[n][1] is a boolean, with True meaning "censor this" and False meaning "print as-is". OUTPUT: The censored text in string form
    censored = ''
    for w in range(len(words)):
    	if words[w][1] == True:
    		words[w][0] = asterisk(words[w][0])
    	censored = censored + words[w][0] + ' '
    return censored

def outputToFile(filename, content):
	# linesToList(stringToLines("Fuck your bitch ass, motherfucker")) 		# to test the list of lists
    with open(filename, 'w') as f:
            f.write(content)
    print "Filtered text has been written to '%s'." % filename 

def fileMain(filename, outputname):
    inlist = linesToList(fileToLines(filename))
    output = main(inlist)
    print "Filtering the contents of %s, and writing them to %s." % (filename, outputname)
    outputToFile(outputname, output)

def main(inputList):
    for w in range(len(inputList)):
        if profaneWords.compare(inputList[w][0]) == True:
            inputList[w].append(True)
        ##elif:
            ##variation check
        else:
            inputList[w].append(False) 
    output = censor(inputList)
    return output

##print linesToList(stringToLines("Fuck your bitch ass, motherfucker")) # to test the list of lists
##print profaneWords.compare('fuck')
##print censor([['Fuck',True],['your',False],['bitch',True],['ass',True]])
