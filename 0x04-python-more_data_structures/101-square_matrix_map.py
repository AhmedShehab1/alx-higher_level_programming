#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squared_matrix = list(map(lamda x: list(map(lambda y: y ** 2, x)), matrix))
    return squared_matrix
