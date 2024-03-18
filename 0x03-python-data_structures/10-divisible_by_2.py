#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return "None"
    else:
        newList = []
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                newList += [True]
            else:
                newList += [False]
        return (newList)
