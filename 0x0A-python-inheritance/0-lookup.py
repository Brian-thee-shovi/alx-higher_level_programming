#!/usr/bin/python3
"""Mods documentation for lists and methods of an object"""


def lookup(obj):
    """func returns list of objects attribute"""

    list_attr = []
    list_meth = []

    for objects in dir (obj):
        if callable(objects):
            list_meth.append(objects)
        else:
            list_attr.append(objects)
    return list_attr + list_meth
