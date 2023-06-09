#!/usr/bin/python3
"""Mods documentation for shape of rectangle"""


class Rectangle():
    """reps the class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the other rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            solution = ""
            _symbol = str(self.print_symbol)
            for ki in range(self.__height - 1):
                solution += (_symbol * self.__width) + '\n'
            solution += _symbol * self.__width
        return solution

    def __repr__(self):
        hi = str(self.__height)
        we = str(self.__width)
        solution = "Rectangle(" + we + ", " + hi + ")"
        return solution

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
