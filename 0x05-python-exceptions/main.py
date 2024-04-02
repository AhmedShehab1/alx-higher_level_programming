#!/usr/bin/python3
safe_print_list = __import__('6-raise_exception_msg').raise_exception_msg
try:
        safe_print_list("C is Fun")
except NameError as te:
        print(te)
