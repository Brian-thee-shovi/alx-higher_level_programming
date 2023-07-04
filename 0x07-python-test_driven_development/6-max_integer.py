#!/usr/bin/python3
"""
this mod to find the max integer in a list
"""


def max_integer(list=[]):
    """
    func to find and return the max integer in a list of integers
    if the list is empty, the func returns None
    """
    if len(list) == 0:
        return None
    resul_t = list[0]
    ki = 1
    while ki < len(list):
        if list[ki] > resul_t:
            resul_t = list[ki]
        ki += 1
    return resul_t
