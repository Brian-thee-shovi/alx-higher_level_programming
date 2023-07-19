#!/usr/bin/python3
"""defines mods documentation for the class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """reps the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """this initializes the class Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the width/size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """gives the value of the size"""
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update the squares"""
        len_args = len(args)
        len_kwargs = len(kwargs)
        my_attributes = ["id", "size", "x", "y"]

        if len_args > 4:
            len_args = 4

        if len_args > 0:
            for ki in range(len_args):
                setattr(self, my_attributes[ki], args[ki])
        elif len_args > 0:
            for _key, v_value in kwargs.items():
                if _key in my_attributes:
                    setattr(self, _key, v_value)

    def to_dictionary(self):
        """returns dict representation of a square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
