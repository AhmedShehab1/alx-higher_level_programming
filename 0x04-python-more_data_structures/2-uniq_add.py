#!/usr/bin/python3
def uniq_add(my_list=[]):
    Sum = 0
    for index, element in enumerate(my_list):
        Flag = 0
        for i in range(index + 1, len(my_list)):
            if element == my_list[i]:
                Flag = 1
                break
        if Flag == 0:
            Sum += element
    return Sum
