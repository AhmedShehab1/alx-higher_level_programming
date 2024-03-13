#!/usr/bin/python3
def uppercase(Ahmed):
    for i, char in enumerate(Ahmed):
        if ord(char) > 96 and ord(char) < 123:
            print("{}{}".format(chr(ord(char) - 32), "\n" if i + 1 == len(Ahmed) else ""), end="")
        else:
            print("{}{}".format(char, "\n" if i + 1 == len(Ahmed) else ""), end="")
