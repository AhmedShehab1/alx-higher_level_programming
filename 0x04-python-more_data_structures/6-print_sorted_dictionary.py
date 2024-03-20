#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        keys = sorted(a_dictionary.keys())
        for i in range(len(a_dictionary)):
            print("{}: {}".format(keys[i], a_dictionary[keys[i]]))
