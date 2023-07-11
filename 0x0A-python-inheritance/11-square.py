#!/usr/bin/python3
"""defines mods documentation"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """reps the class square"""

    def __init__(self, size):
        """initializes the class square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """it gives the area of a square"""

        return self.__size * self.__size
