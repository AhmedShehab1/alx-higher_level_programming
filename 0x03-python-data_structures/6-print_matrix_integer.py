#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for List in matrix:
        for int in List:
            if len(List) - 1 != List.index(int):
                print("{:d}".format(int), end=" ")
            else:
                print("{:d}".format(int), end="")
        print("")
