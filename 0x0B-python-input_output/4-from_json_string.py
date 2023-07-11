#!/usr/bin/python3
"""defines mods documentation for json returns of python data"""


import json


def from_json_string(my_str):
    """
    func that returns a python object which is reped by
    python string
    """
    return json.loads(my_str)
