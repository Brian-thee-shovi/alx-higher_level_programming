#!/usr/bin/python3
"""Mods documentation for lists and methods of an object"""


def lookup(obj):
    """func returns list of objects attribute"""

    lista_ttribute = []
    listm_ethod = []

    for objects in dir(obj):
        if callable(objects):
            listm_ethod.append(objects)
        else:
            lista_ttribute.append(objects)
    return lista_ttribute + listm_ethod
