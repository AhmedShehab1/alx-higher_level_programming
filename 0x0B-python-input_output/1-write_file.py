#!/usr/bin/python3
"""Module That Defines Methods To Write To Python Stream Objects"""


def write_file(filename="", text=""):
    """
    Method To Write Provided <text> in file
    specified in given <filename>
    ^ Overwrites file Content
    ^ Create File If Doesnt Exist
    Args:
        filename (str, optional): String Representation
                                  of File To Write To. Defaults to "".

        text (str, optional): Text That Will Overwrites
                              file Content. Defaults to "".
    """
    with open(filename, mode="w", encoding='utf-8') as file:
        return (file.write(text))
