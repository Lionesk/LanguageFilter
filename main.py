import sys, os, os.path
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

def main():

    inputList = []
    print "LanguageFilter Beta -- By Emilio Assuncao and Liam Bassford"
    goodInput = False
    while(goodInput != True):
        # CHANGE BACK!!!
        choice = 'f'# raw_input("Type f to input a filename and s to type a string.\n").lower()
        if(choice == 'f'):
            fileName = 'carlin.txt'# raw_input("Enter the name of your file (must me in same directory).\n").lower()
            if(os.path.isfile(fileName)):
                inputList = linesToList(fileToLines(fileName))
                goodInput = True
            else:
                print "File does not exist in directory."
        elif(choice == 's'):
            inputString = input("Type the string you would like to filter.\n").lower()
            inputList = linesToList(stringToLines(inputString))
            goodInput = True
        else:
            print "Input not recognized, please try again."
    # print inputList #- for debugging
    for w in range(len(inputList)):
        # print inputList[w][0]
        context = []
        if w-10 < 0 and w+10 >= len(inputList):
            context = inputList[0:len(inputList)]
        elif w-10 < 0 and w+10 < len(inputList):
            context = inputList[0:w+10]
        elif w-10 >= 0 and w+10 >= len(inputList):
            context = inputList[w-10:len(inputList)]
        else:
            context = inputList[w-10:w+10]
        # print context
        contextCopy = []
        for i in range(len(context)):
            contextCopy.append(context[i])
        inputListCopy = []
        for i in range(len(inputList)):
            inputListCopy.append(inputList[i])
        if profaneWords.compare(inputListCopy[w][0], contextCopy) == True:
            inputList[w].append(True)
        ##elif:
            ##variation check
        else:
            inputList[w].append(False) 
        # print inputList[w]
    output = censor(inputList)
#    print inputList
    print "Here is the filtered text."
    print output

# linesToList(stringToLines("Fuck your bitch ass, motherfucker")) # to test the list of lists
    with open('results.txt', 'w') as f:
            f.write(output)
    print "Filtered text has been written to 'results.txt'." 

##print linesToList(stringToLines("Fuck your bitch ass, motherfucker")) # to test the list of lists
##print profaneWords.compare('fuck')
main()
##print censor([['Fuck',True],['your',False],['bitch',True],['ass',True]])
