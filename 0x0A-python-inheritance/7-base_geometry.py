#!/usr/bin/python3
"""
defines mods documentation for base geometry
"""


class BaseGeometry():
    """ reps the class BaseGeometry"""

    def area(self):
        """finds the area"""
        raise Exception("area() is not implemented")

    def interger_validator(self, name, value):
        """this validates type of value"""
        if (not type(value) is int):
            raise TypeError("{:s} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
