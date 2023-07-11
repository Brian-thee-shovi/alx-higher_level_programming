#!/usr/bin/python3
"""module documentation for my code"""


def class_to_json(obj):
    """
    func returns dictionary description for
    the json serailization
    """
    return obj.__dict__
