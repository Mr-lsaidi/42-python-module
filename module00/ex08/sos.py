import sys

morse_code = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ' ': '/'}

if len(sys.argv) > 1:
    str = (' ').join(sys.argv[1::]).upper()
    try:
        morse = ""
        i = 0
        while i < len(str):
            c = str[i]
            if not c in morse_code.keys():
                raise ValueError("ERROR")
            else:
                morse += morse_code[c]
            i += 1
            if not i == len(str):
                morse += " "
        print(morse)
    except Exception as e:
        print(e)
