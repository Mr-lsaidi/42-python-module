import sys

result = []
for arg in sys.argv[:0:-1]:
    revert = arg[::-1]              #reverse the string
    swapCase = revert.swapcase()    #swap cases
    result.append(swapCase)
    
print((' ').join(result))           #join the array to string with ' ' as separator