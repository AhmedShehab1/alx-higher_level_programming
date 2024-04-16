#!/usr/bin/python3
""" Module Designed To Read From A Specified
    File And Print File's Content To Stdout
"""


def read_file(filename=""):
    """
    Function To Print File Content To Stdout
    Args:
        filename (str, empty): String Representing File Name. Defaults to "".
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
