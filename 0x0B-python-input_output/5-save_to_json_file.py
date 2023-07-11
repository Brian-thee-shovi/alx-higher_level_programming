#!/usr/bin/python3
"""mod documentation defining a json file writing func"""


import json


def save_to_json_file(my_obj, filename):
    """
    func writes an object file in a text file using
    json represetation
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
