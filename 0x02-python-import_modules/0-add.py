#!/usr/bin/python3
"""prints the result of the addition 1 + 2 = 3"""
from add_0 import add


if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
