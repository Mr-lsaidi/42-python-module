from count import text_analyzer
text1 = "Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles."
text2 = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
text3 = ""


# print ("------|empty param|------\n")
# text_analyzer("")

# print ("------|no param|------\n")
# text_analyzer()

# print ("------| __doc__ |-----\n")
# print(text_analyzer.__doc__)

print ("------|text 1|------\n")
print ('text : {}\n'.format(text1))
text_analyzer(text2)
print ("------|text 2|------\n")
print ('text : {}\n'.format(text2))
text_analyzer(text2)
