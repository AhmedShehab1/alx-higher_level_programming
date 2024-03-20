#!/usr/bin/python3
def printed_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())
    for i in range(len(a_dictionary)):
        print("{}: {}".format(keys[i], a_dictionary[keys[i]]))
