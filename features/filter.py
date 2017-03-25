from features import profaneWords

# The meat of the program, this function takes as input a list of words and goes through the lines of filtering by
# calling functions from the supporting python files. A list of lists is produced, where the second cell keeps track of
# whether something is meant to be filtered with [1] as either True or False. Once all the lines of filtering are
# complete, the function calls the censor function which looks at that boolean value and censors it by calling the
# asterisk function.
from utils.lines import linesToList, fileToLines


def filtertext(inputList):
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


def outputToFile(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print("Filtered text has been written to '%s'." % filename)


def fileMain(filename, outputname):
    inlist = linesToList(fileToLines(filename))
    output = main(inlist)
    print("Filtering the contents of %s, and writing them to %s." % (filename, outputname))
    outputToFile(outputname, output)