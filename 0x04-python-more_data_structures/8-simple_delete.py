#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == "":
        return
    a_dictionary[key] = 0
    a_dictionary.pop(key)
    return a_dictionary
