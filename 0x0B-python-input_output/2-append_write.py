#!/usr/bin/python3
"""defines mods for appending a text in a file"""


def append_write(filename="", text=""):
    """func appends a text to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
