#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("{}".format(i // 10), end="")
    print("{}{}".format(i, "\n" if i == 99 else ", "), end="")
