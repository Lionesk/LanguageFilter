import sys
import bannedWords

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


