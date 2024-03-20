#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = dict(a_dictionary)
    for i in newDict:
        newDict[i] = newDict[i] * 2
    return newDict
