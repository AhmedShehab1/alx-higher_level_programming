#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return [ ]
    newMatrix = list(matrix)
    for i, j in enumerate(newMatrix):
        newMatrix[i] = list(map(lambda x: x ** 2, j))
    return newMatrix
