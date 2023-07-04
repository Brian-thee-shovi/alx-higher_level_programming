#!/usr/bin/python3
"""
This is a mod to prints a square
"""


def print_square(size):
    """
    func that prints a square with '#'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for ki in range(size):
        print("#" * size)
