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
    print output2
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
        choice = raw_input("Type f to input a filename and s to type a string.\n").lower()
        if(choice == 'f'):
            fileName = raw_input("Enter the name of your file (must me in same directory).\n").lower()
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
    ##print inputList - for debugging
    for pos, w in enumerate(inputList):
        if profaneWords.compare(w) == True:
            inputList[pos][1].append(True)
        ##elif:
            ##variation check
        else:
            inputList[pos][1].append(False) 
    output = censor(inputList)
    print "Here is the filtered text."
    print output

# linesToList(stringToLines("Fuck your bitch ass, motherfucker")) # to test the list of lists

 main()
##print censor([['Fuck',True],['your',False],['bitch',True],['ass',True]])
