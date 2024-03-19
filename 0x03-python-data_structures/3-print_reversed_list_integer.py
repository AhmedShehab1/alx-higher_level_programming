#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return []
    Len = len(my_list)
    for i in range(Len):
        print("{:d}".format(my_list[Len - (i + 1)]))
