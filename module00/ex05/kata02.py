t = (3, 30, 2019, 9, 25)


month = ""
day = ""
year = ""
hour = ""
min = ""
if (len(t) != 5):
    print("you need to pass 5 elemets in the tuple")
else :
    if t[3] < 10:
        month = "0"
    if t[4] < 10:
        day = "0"
    if t[2] < 1000:
        year = "0"
    if t[2] < 100:
        year = "00"
    if t[2] < 10:
        year= "000"
    if t[0] < 10:
        h = "0"
    if t[1] < 10:
        min = "0"
    print("{}{}/{}{}/{}{} {}{}:{}{}"
          .format(month, t[3], day, t[4], year, t[2], hour, t[0], min, t[1]))