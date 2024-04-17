#!/usr/bin/python3
"""
Module For JSON Files Encoding
"""
import json


def from_json_string(my_str):
    """
    Function that Returns a Python Data Structure represented by a JSON String
    Args:
        my_str (str): String

    Returns:
        Object: Python Data Structure
    """
    return json.loads(my_str)
