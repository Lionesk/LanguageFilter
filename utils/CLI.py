import os
import os.path
from .lines import *


# A recipe we pulled from the web for implementing a switch feature in Python, very useful for the CLI.
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


# The banner that appears at the top of the program. Clears the command line (cross platform) to make the program look clean.
def asciibanner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("################################################################")
    print("  _                                        ___ _ _ _           ")
    print(" | |   __ _ _ _  __ _ _  _ __ _ __ _ ___  | __(_) | |_ ___ _ _ ")
    print(" | |__/ _` | ' \/ _` | || / _` / _` / -_) | _|| | |  _/ -_) '_|")
    print(" |____\__,_|_||_\__, |\_,_\__,_\__, \___| |_| |_|_|\__\___|_|  ")
    print("                |___/          |___/                           ")
    print("################################################################")
    print("Version 0.1 #################### Liam Bassford & Emilio Assuncao")
    print("\n\n\n")


# Basic information about the program. Called by the menu function when the user inputs the command.
def info():
    print("\n##########")
    print("Composed of languagefilter.py, main.py, ProfaneWords.py, variations.py,\nand all the other supporting "
          "documents this program uses many\nlines of filtering to optimize the removal of foul language.\n")
    print("This CLI made possible with patorjk.com and code.activestate.com/recipes/410692")
    print("##########\n\n\n")


# The meat of the CLI. The menu is a bootstraped python switch within a while loop that waits for exit to be selected
# by the user. Gives the user the option to input from a string or from files, the latter further offering the option to
# write to a file or to the command line. The while loop calles the banner every time to give the illusion of a GUI, where
# the same things are up on screen all the time. At the end of every line in the branch the program waits for a carriage
# return from the user with raw_input, this lets the user choose when to move on and refresh the screen.
def cli():
    exit = False
    while (exit == False):
        asciibanner()
        print("Main menu:")
        print("k: Filter from keyboard input.")
        print("t: Filter a text file.")
        print("x: Exit.")
        print("i: About this program.\n")
        o = input(":")
        for case in switch(o):
            if case('x'):
                print("\nExiting the program.")
                exit = True
                break
            if case('i'):
                info()
                input("Continue...")
                break
            if case('k'):
                print("\nType in the string you would like to filter.\n")
                rawInput = input(":")
                print("\nHere is the filtered string:")
                print(main(linesToList(stringToLines(rawInput))))
                input("Continue...\n")
                print("\n\n\n")
                break
            if case('t'):
                filename = input("\nPlease enter the name of the file.\n:")
                while os.path.exists(filename):
                    print("File couldn't be found.")
                    filename = input("\nPlease enter the name of the file.\n:")
                print("Would you like to write the results to a text file?\n(y/n)")
                t = input(":")
                for case in switch(t):
                    if case('y'):
                        outfilename = input("\nEnter a name for the output file. (Default is results.txt)\n:")
                        if outfilename == '':
                            outfilename = 'results.txt'
                        fileMain(filename, outfilename)
                        break
                    if case('n'):
                        print("\nHere is the filtered text:")
                        print(main(linesToList(fileToLines(filename))))
                        break
                    if case():
                        print("\nIncorrect input.")
                        break
                input("Continue...\n")
                print("\n\n\n")
                break
            if case():
                print("\nIncorrect input.\n\n\n")
                break

