#!/usr/bin/python3
import json
"""
Module To Convert Python Object To Its Equivalent JSON Representation
"""


def to_json_string(my_obj):
    """
    function that returns the JSON
    representation of an object (string):
    Args:
        my_obj (object): Python Object (i.e. Dict ... etc.)

    Returns:
        str: Json Representation
    """
    return json.dumps(my_obj)
