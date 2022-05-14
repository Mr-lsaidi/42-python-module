import re
import sys

def text_analyzer(*args):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.."""
    if (len(args) == 0):
        print("What is the text to analyse?")
        print(">> ",end = '')
        sys.stdout.flush()
        string = sys.stdin.readline()
    elif (len(args) == 1): 
        string = args[0]
    elif (len(args) > 1):
        print ("ERROR")
        exit()
    upperCase = len(re.findall(r'[A-Z]',string))
    lowerCase = len(re.findall(r'[a-z]',string))
    punctuateChar = len(re.findall(r'[!?,.;\'\"-]',string))
    spaces = len(re.findall(r'[ \t\n\r\v\f]',string))

    print ("{} upper letters".format(upperCase))
    print ("{} lower letters".format(lowerCase))
    print ("{} punctuation marks".format(punctuateChar))
    print ("{} spaces".format(spaces))


