#!/usr/bin/python3
"""defines mods documentation"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """reps a subclass Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """this outputs area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns string of an instance of class rectangle"""
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
