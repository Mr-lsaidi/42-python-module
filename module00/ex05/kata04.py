t = (0, 4, 132.42222, 10000, 12345.67)

if (len(t) != 5):
    print("you need to pass 5 elemets in the tuple")
else:
    module = "module_"
    ex = "ex_"
    if (t[0] < 10):
        module += "0"
    if (t[1] < 10):
        ex += "0"

    print('{}{}, {}{} : {:.2f}, {:.2e}, {:.2e}'.format(module, t[0], ex, t[1], t[2], t[3], t[4]))
