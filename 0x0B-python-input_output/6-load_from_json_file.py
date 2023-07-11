#!/usr/bin/python3
"""mods documentation defining json reading func"""


import json


def load_from_json_file(filename):
    """func creates an object from a json file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
