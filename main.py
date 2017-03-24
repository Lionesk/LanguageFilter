
import profaneWords, variations


# A function that takes a filename, tries to find it in the directory and then creates a list of lines.
def fileToLines(filename):
    openedFile = open(filename, 'r')
    lines = openedFile.read().splitlines()
    openedFile.close()
    return lines


# INPUT: a string. OUTPUT: a list of lines.
def stringToLines(string):
    lines = string.splitlines()
    return lines


# INPUT: a list of lines. OUTPUT: a list of words.
def linesToList(lines):
    output = []
    for l in lines:
        for w in l.split():
            output.append(w)
    output2 = [[] for s in range(len(output))]
    for s in range(len(output)):
        output2[s].append(output[s])  # makes into list of lists format
    return output2


def asterisk(s):
    # INPUT: a string. OUTPUT: that string, with all characters except the first replaced with asterisks
    if len(s) < 3:
        return s
    cens = ''
    cens = cens + s[0]
    for n in range(len(s) - 2):
        cens = cens + '*'
    cens = cens + s[len(s) - 1]
    return cens


def censor(words):
    # INPUT: a list of lists. For each sublist, words[n][0] is a word, and words[n][1] is a boolean, with True meaning
    # "censor this" and False meaning "print as-is". OUTPUT: The censored text in string form
    censored = ''
    for w in range(len(words)):
        if words[w][1] == True:
            words[w][0] = asterisk(words[w][0])
        censored = censored + words[w][0] + ' '
    return censored


# Rudimentary write to file function.
def outputToFile(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print("Filtered text has been written to '%s'." % filename)


# This is the function that is called from languagefilter.py when output to file is selected. It opens the file
# converts the data into a list and passes that to the main function. When it receives the output from main it writes it
# using the method.
def fileMain(filename, outputname):
    inlist = linesToList(fileToLines(filename))
    output = main(inlist)
    print("Filtering the contents of %s, and writing them to %s." % (filename, outputname))
    outputToFile(outputname, output)


# The meat of the program, this function takes as input a list of words and goes through the lines of filtering by
# calling functions from the supporting python files. A list of lists is produced, where the second cell keeps track of
# whether something is meant to be filtered with [1] as either True or False. Once all the lines of filtering are
# complete, the function calls the censor function which looks at that boolean value and censors it by calling the
# asterisk function.
def main(inputList):
    cs = 5  # context size
    for w in range(len(inputList)):
        context = []
        if w - cs < 0 and w + cs >= len(inputList):
            context = inputList[0:len(inputList)]
        elif w - cs < 0 and w + cs < len(inputList):
            context = inputList[0:w + cs]
        elif w - cs >= 0 and w + cs >= len(inputList):
            context = inputList[w - cs:len(inputList)]
        else:
            context = inputList[w - cs:w + cs]
        contextCopy = []
        for i in range(len(context)):
            contextCopy.append(context[i])
        inputListCopy = []
        for i in range(len(inputList)):
            inputListCopy.append(inputList[i])
        # print contextCopy
        if profaneWords.compare(inputListCopy[w][0], contextCopy) == True:
            inputList[w].append(True)
            ##elif:
            ##variation check
        else:
            inputList[w].append(False)
    output = censor(inputList)
    return output
