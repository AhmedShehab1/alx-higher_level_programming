#!/usr/bin/python3
"""
Module That Contains Methods To Append Content At The End Of A File

"""


def append_write(filename="", text=""):
    """
    Method To Append New Content Provided In <text>
    At The End Of file  Specified with <filename>
    Args:
        filename (str, optional): String Representation
                                  Of File Name. Defaults to "".

        text (str, optional): Content To Be Added At
                              The End Of The File. Defaults to "".
    """
    with open(filename, mode="a", encoding='utf-8') as file:
        return (file.write(text))
