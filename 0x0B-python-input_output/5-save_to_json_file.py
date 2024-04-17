#!/usr/bin/python3
"""
Module For JSON Decoding
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function That Writes An Object To A Text File
    Using JSON Representation
    Args:
        my_obj (Object): Python Data Structure
        filename (str): Name Of The File
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
