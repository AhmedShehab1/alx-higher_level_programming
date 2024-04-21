#!/usr/bin/python3
"""
Module For JSON Encoding
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

cmd_line_arguments = sys.argv[1:]
try:
    cmd_line_arguments = load_from_json_file("add_item.json")\
        + cmd_line_arguments
    save_to_json_file(cmd_line_arguments, "add_item.json")
except Exception:
    save_to_json_file(cmd_line_arguments, "add_item.json")
