#!/usr/bin/python3
"""defines mod documentation"""


def inherits_from(obj, a_class):
    """
    checks if obj is an inherited instance of a class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
