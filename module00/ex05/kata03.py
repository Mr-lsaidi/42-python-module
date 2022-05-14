phrase = "The right format"
leng = len(phrase)
if (leng <= 42):
    print("-" * (42 - leng) + phrase, end="")
else:
    print("the word too long :")
    print(phrase)
