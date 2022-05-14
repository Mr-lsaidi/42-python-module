import sys
argc = len(sys.argv)

def check_number(str):
    sign = False
    tmp = str
    if (str[0] == '+'):
        print("AssertionError: argument is not integer")
        exit()
    if (str[0] == '-'):
        sign = True
        tmp = str[1::]
    try:
        input = int(tmp)
        if (sign):
            input *= -1
        return (input)
    except ValueError:
        print("AssertionError: argument is not integer")
        exit()

def evenOrOdd(nb):
    return nb % 2

if argc > 1:
    if argc == 2:
        value = check_number(sys.argv[1])
        if (value == 0):
            print ("I'm Zero.") 
        elif (value % 2 == 0):
            print ("I'm Even.") 
        else : 
            print ("I'm Odd.")
    else:
        print ("AssertionError: more than one argument is provided")