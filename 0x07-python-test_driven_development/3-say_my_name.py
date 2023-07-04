#!/usr/bin/python3
"""
its module wich says my name
"""


def say_my_name(first_name, last_name=""):
    """
    func that prints the name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    my_name = first_name + last_name
    if last_name:
        my_name = first_name + " " + last_name
    else:
        my_name = first_name + " "
    print("My name is", my_name)
