#!/usr/bin/python3
def uppercase(Ahmed):
    for i, char in enumerate(Ahmed):
        if ord(char) > 96 and ord(char) < 123:
            print("{}".format(chr(ord(char) - 32)), end="")
        else :
            print("{}".format(char), end="")
