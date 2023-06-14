#!/usr/bin/python3
import sys


if __name__ == "__main__":
    """prints the number of and the list of its arguments"""

    list_1 = sys.argv
    func_len = len(list_1) - 1

    if func_len == 0:
        print(func_len, "arguments.")
    elif func_len == 1:
        print(func_len, "argument:")
        for ram in range(1, func_len + 1):
            print("{:d}: {}".format(ram, list_1[ram]))
    elif func_len > 1:
        print(func_len, "arguments:")
        for zi in range(1, func_len + 1):
            print("{:d}: {}".format(zi, list_1[zi]))
