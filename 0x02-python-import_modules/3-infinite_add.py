#!/usr/bin/python3
import sys
if __name__ == "__main__":
    Sum = 0
    for i, j in enumerate(sys.argv):
        if i == 0:
            continue
        Sum += int(j)
    print(Sum)
