import re
import sys

try:
    if len(sys.argv) == 3:
        if not bool(sys.argv[1]) or not sys.argv[2].isdigit():
            raise ValueError("ERROR")
        else:
            number = int(sys.argv[2]) + 1
            regex = '\w{'+str(number)+',}'
            m = re.findall(regex, sys.argv[1])
            print(m)
except Exception as e:
    print(e)