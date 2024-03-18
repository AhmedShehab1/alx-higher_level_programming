#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newTuple = ()
    tuple_a = initializeEmptyTuple(tuple_a)
    tuple_b = initializeEmptyTuple(tuple_b)
    for i in range(2):
        newTuple += (tuple_a[i] + tuple_b[i],)
    return newTuple


def initializeEmptyTuple(Tuple):
    if len(Tuple) < 2:
        while len(Tuple) != 2:
            Tuple += (0,)
    return Tuple
