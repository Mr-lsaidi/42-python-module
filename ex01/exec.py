import sys

for arg in sys.argv[:0:-1]:

    if len(arg):
        revert = arg[::-1] #reverse the string
        swapCase = revert.swapcase()  #swap cases
        print(swapCase)
