#!/usr/bin/python3
"""
define module documentation
"""


class Square():
    """
    class representing a square
    """

    def __init__(self, size=0):
        """
        initialize another square

        Args:
            size (int): size of the other square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
