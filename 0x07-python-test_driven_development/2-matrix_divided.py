#!/usr/bin/python3
"""
Module For Operations On Matrices
"""


def matrix_divided(matrix, div) -> list:
    Flag = 0
    if matrix is not None:
        if isinstance(matrix, list):
            if isinstance(matrix[0], list) and isinstance(matrix[1], list):
                if len(matrix[0]) == len(matrix[1]):
                    if  isinstance(div, (int, float)):
                        if div == 0:
                            raise ZeroDivisionError("division by zero")
                    else:
                        raise TypeError("div must be a number")
                    for row in matrix:
                        for element in row:
                            if not isinstance(element, (int, float)):
                                Flag = 1
                                break
                    if Flag == 0:
                        return [*map(lambda sublist: [round(x / div, 2) for x in sublist], matrix)]
                else:
                    raise TypeError("Each row of the matrix must have the same size")
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")