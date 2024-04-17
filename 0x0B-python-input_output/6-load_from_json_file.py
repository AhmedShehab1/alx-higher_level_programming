#!/usr/bin/python3
import json
"""
Module For JSON Files Encoding
"""


def load_from_json_file(filename):
    """
    Function That Creates An Object From A JSON File
    Args:
        filename (str): Name Of File

    Returns:
        object: Python Data Structure
    """
    with open(filename, encoding='utf-8')as file:
        return json.loads(file.read())
