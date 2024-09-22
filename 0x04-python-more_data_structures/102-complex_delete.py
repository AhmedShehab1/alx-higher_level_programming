#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary:
        to_be_deleted = [k for k, v in a_dictionary.items() if v == value]
        for k in to_be_deleted:
            del a_dictionary[k]
        return a_dictionary
