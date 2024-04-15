#!/usr/bin/python3
"""Module That Shows Inheritance from list class"""


class MyList(list):
    """
    class MyList that inherits from list:
    Args:
        list (Class): MyList Class Inherits From it
    """

    def print_sorted(self):
        """
        Method To prints the list, but sorted (ascending sort)
        """
        list_cp = self[:]
        for i in range(len(list_cp)):
            for j in range(i, len(list_cp)):
                if list_cp[i] > list_cp[j]:
                    temp = list_cp[j]
                    list_cp[j] = list_cp[i]
                    list_cp[i] = temp
        print(list_cp)
