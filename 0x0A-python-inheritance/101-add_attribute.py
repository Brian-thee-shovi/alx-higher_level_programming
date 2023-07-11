#!/usr/bin/python3
"""defines mod documentation"""


def add_attribute(objct, n_attribute, value_attr):
    """ method that adds an attribute"""
    if not hasattr(objct, "__dict__"):
        raise TypeError("can't add new attribute")
    objct.__dict__[n_attribute] = value_attr
