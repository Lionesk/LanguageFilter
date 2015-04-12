import sys
import bannedWords
import cgi, cgitb
import profaneWords

#allowing for traceback errors and messages
cgitb.enable()

##Setting up the necessary code to accept the text from the website it raw form
##using the CGI post method
form = cgi.FieldStorage()
raw_text = form.getvalue('raw')

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

##main code for this applet
line = stringToLines(raw_text)
##first line of censorship
for l in line:
    for w in l:
        if profaneWords.compare(w) == True:
            w = profaneWords.censor(w)


