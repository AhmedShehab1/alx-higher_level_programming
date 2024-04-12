#!/usr/bin/python3
"""
Module To Manipulate Given String
"""

def text_indentation(text):
    start_position = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char_no, letter in enumerate(text):
        if letter in ['.', '?', ':']:
            print(text[start_position: char_no + 1], end="\n\n")
            try:
                while text[char_no + 1] == ' ':
                    char_no += 1
            except:
                pass
            else:
                start_position = char_no + 1
