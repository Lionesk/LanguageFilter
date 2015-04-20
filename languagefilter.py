import sys, os, os.path
from main import fileToLines, stringToLines, linesToList, main, fileMain

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False

def ascii():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "################################################################"
    print "  _                                        ___ _ _ _           "
    print " | |   __ _ _ _  __ _ _  _ __ _ __ _ ___  | __(_) | |_ ___ _ _ "
    print " | |__/ _` | ' \/ _` | || / _` / _` / -_) | _|| | |  _/ -_) '_|"
    print " |____\__,_|_||_\__, |\_,_\__,_\__, \___| |_| |_|_|\__\___|_|  "
    print "                |___/          |___/                           "
    print "################################################################"
    print "Version 0.1 #################### Liam Bassford & Emilio Assuncao"
    print "\n\n\n"

def info():
    print "\n##########"
    print "Composed of languagefilter.py, main.py, ProfaneWords.py, variations.py,\n this program uses many lines of filtering to optimize the removal of foul language.\n"
    print "This CLI made possible with patorjk.com and code.activestate.com/recipes/410692"
    print "##########\n\n\n"

def menu():
    ascii()
    exit = False
    while(exit == False):
        print "Main menu:"
        print "k: Filter from keyboard input."
        print "t: Filter a text file."
        print "x: Exit."
        print "i: About this program.\n"
        o = raw_input(":")
        for case in switch(o):
            if case('x'):
                print "\nExiting the program."
                exit = True
                break
            if case('i'):
                info()
                raw_input("Continue...")
                break
            if case('k'):
                print "\nType in the string you would like to filter.\n"
                rawInput = raw_input(":")
                print "\nHere is the filtered string:"
                print main(linesToList(stringToLines(rawInput)))
                raw_input("Continue...\n")
		print "\n\n\n"
                break
            if case('t'):
                filename = raw_input("\nPlease enter the name of the file.\n:")
                while os.path.exists(filename) == False:
                    print "File couldn't be found."
                    filename = raw_input("\nPlease enter the name of the file.")
                print "Would you like to write the results to a text file?\n(y/n)"
                t = raw_input(":")
                for case in switch(t):
                    if case('y'):
                        outfilename = raw_input("\nEnter a name for the output file. (Default is results.txt)\n:")
                        if(outfilename == ''):
                            outfilename = 'results.txt'
                        fileMain(filename, outfilename)
                        break
                    if case('n'):
                        print "\nHere is the filtered text:"
                        print main(linesToList(fileToLines(filename)))
                        break
                    if case():
                        print "\nIncorrect input."
                        break
                raw_input("Continue...\n")
		print "\n\n\n"                
		break
            if case():
                print "\nIncorrect input.\n\n\n"
                break

#calling the menu fucntion which serves as the main
menu()
