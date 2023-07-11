#!/usr/bin/python3
"""defines mods documentation for writing in a text file"""


def write_file(filename="", text=""):
    """
    func writes astr in a text file and returns
    num of char written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
