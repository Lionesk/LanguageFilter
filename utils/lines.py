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

