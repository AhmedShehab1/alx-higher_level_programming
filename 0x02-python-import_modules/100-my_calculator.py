#!/usr/bin/python3
from sys import argv as av
import calculator_1 as cc
if __name__ == "__main__":
    if len(av) - 1 != 3:
        print("Usage: {} <a> <operator>\
 <b>".format(av[0]))
        exit(1)
    if av[2] != '+' and\
        av[2] != '-' and\
        av[2] != '*' and\
        av[2] != '/':
        print("Unknown operator. Available operators:\
 +, -, * and /")
        exit(1)
    print("{} {} {} = {}"\
        .format(av[1], av[2],\
            av[3], cc.add(int(av[1]),\
            int(av[3])) if av[2] == '+'\
            else cc.sub(int(av[1]), int(av[3]))\
            if av[2] == '-' else\
            cc.mul(int(av[1]), int(av[3]))\
            if av[2] == '*' else\
            cc.div(int(av[1]), int(av[3]))))
