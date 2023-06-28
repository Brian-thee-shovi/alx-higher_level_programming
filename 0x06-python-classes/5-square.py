#!/usr/bin/python3
"""
define module documentation
"""


class Square():
    """
    class that reps a square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

        def area(self):
            """
            cal and return the area of a square
            """
            return self.__size ** 2

        def my_print(self):
            if self.__size == 0:
                print()
                return None
            for v in range(self.__size):
                for h in range(self.__size):
                    print("#", end="")
                print()
