import sys

def check_number(str):
    sign = False
    tmp = str
    if (str[0] == '+'):
        print("InputError: only numbers\n")
        print("Usage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3")
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
        print("InputError: only number\n")
        print("Usage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3")
        exit()


if (len(sys.argv) == 3):
    number1 = check_number(sys.argv[1])
    number2 = check_number(sys.argv[2])

    addition = number1 + number2
    diff = number1 - number2
    multi = number1 * number2
    print('Sum:        {}'.format(addition))
    print('Difference: {}'.format(diff))
    print('Product:    {}'.format(multi))
    try:
        div = number1 / number2
        print('Quotient:   {}'.format(div))
    except:
        print("ERROR (div by zero)")
    try:
        mod = number1 % number2
        print('Remainder:  {}'.format(mod))
    except:
        print("ERROR (modulo by zero)")
else:
    if (len(sys.argv) > 3):
        print("InputError: too many arguments\n")
    print("Usage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3")
