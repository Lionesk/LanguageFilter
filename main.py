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

def linesToList(lines):
    output = []
    for l in lines:
        for w in l:
            output.append(w)
    return output

##main code for this applet
line = stringToLines(raw_text)
##first line of censorship
for l in line:
    for w in l:
        if profaneWords.compare(w) == True:
            w = profaneWords.censor(w)

print """
<html>
    <head>
        <title>Censored text - result.html</title>
        <style>
            p {
                border:1px solid red;
                padding:10px;
                margin:30px;
            }
        </style>
    </head>
    <body>
        <center><p><font size = "5">Results from the filtering program:</font></p></center>
        <br><br><br>
        <form method="post" action="result.cgi">
            <output type="text" name="censored"/>
        </form>
    </body>
    </html>
""" % cgi.escape(message)
