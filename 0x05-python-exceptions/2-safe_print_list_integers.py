#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    Count = 0
    try:
        for i in range(x):
            if type(my_list[i]) != int:
                continue
            print("{:d}".format(my_list[i]), end="")
            Count += 1
        print("")
        return (Count)
    except IndexError as ie:
        raise ie
