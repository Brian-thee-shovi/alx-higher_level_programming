#!/usr/bin/python3
"""
define module documentation
"""


class Square():
    """class that reps a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize another square.

        Args:
            size (int): size of the other square
            position (int, int): position of other square.
        """
        self.size = size
        self.position = position

        @property
        def size(self):
            """sets the current size of the square."""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            @property
            def position(self):
                """sets the current position of the square."""
            return (self.__position)

            @position.setter
            def position(self, value):
                if (not isinstance(value, tuple) or
                    len(value) != 2 or
                    not all(isinstance(num, int) for num in value) or
                        not all(num >= 0 for num in value)):
                    raise TypeError("position must be a tuple of +2 int")
            self.__position = value

            def area(self):
                """return the current area of the square."""
                return (self.__size * self.__size)

            def my_print(self):
                """prints square with the # character."""
                if self.__size == 0:
                    print("")
                    return

                [print("") for v in range(0, self.__position[1])]
                for v in range(0, self.__size):
                    [print(" ", end="") for h in range(0, self.__position[0])]
                    [print("#", end="") for w in range(0, self.__size)]
                    print("")