#!/usr/bin/python3
"""defines mods documentation for json representing it"""


import json


def to_json_string(my_obj):
    """
    func uses json converting data read from the
    text file to strings
    """
    return json.dumps(my_obj)
