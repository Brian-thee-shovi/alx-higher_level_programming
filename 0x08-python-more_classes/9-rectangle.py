#!/usr/bin/python3
"""Mods documentation for the rectangle shape"""


class Rectagle():
    """reps a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the class"""

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """rectangle with greater area is returned"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise ValueError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """new rectangle is returned instance"""
        return (cls(size, size))

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
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
