#!/usr/bin/python3
"""
mod to print two lines after few special characters
"""


def text_indentation(text):
    """
    func prints text with 2 lines after '.','?',':'
    """
    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")
    _str_s = text.split()
    _str_s = " ".join(_str_s)
    _str_s = _str_s.replace(".", ".\n\n")
    _str_s = _str_s.replace(":", ":\n\n")
    _str_s = _str_s.replace("?", "?\n\n")
    _str_s = _str_s.replace("\n ", "\n")

    print(_str_s, end='')
