#!/usr/bin/python3
"""defines mods documentation for reading a textfile"""


def read_file(filename=""):
    """reps func that reads a text file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            print("{}".format(line), end="")
