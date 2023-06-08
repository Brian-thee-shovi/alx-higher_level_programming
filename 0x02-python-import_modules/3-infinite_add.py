#!/usr/bin/python3
import sys


if __name__ == "__main__":
    list_m = sys.argv[1:]
    total = 0
    for me in list_m:
        total = total + int(me)
        print(total)
