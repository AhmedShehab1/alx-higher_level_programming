#!/usr/bin/python3
"""
Module To Manipulate Given String
"""


def text_indentation(text: str):
    """
    function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    Args:
        text (str): Text To Be Indented

    Raises:
        TypeError: If Given Text Is Not Of Type str
    """
    start_position = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char_no, letter in enumerate(text):
        if letter in ['.', '?', ':']:
            print(text[start_position: char_no + 1], end="\n\n")
            try:
                while text[char_no + 1] == ' ':
                    char_no += 1
            except Exception:
                pass
            else:
                start_position = char_no + 1
