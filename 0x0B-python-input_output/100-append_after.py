#!/usr/bin/python3
"""
mods documentation defining a text file insertion func
"""


def append_after(filename="", search_string="", new_string=""):
    """
    func inserts a text afetr each line
    containing a given string in a file
    """
    text = ""
    with open(filename) as ki:
        for line in ki:
            text = tet + line
            if search_string in line:
                text = text + new_string

    with open(filename, "w") as w:
        w.write(text)
