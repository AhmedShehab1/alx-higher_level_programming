#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) - 1 == 0:
        print("{} arguments.".format(0))
    else:
        print("{} {}".format(len(sys.argv) - 1, \
            "argument:" if len(sys.argv) - 1 == 1 else \
                "arguments:"))
        for i, j in enumerate(sys.argv):
            if i == 0:
                continue
            print("{}: {}".format(i, j))
