#!/usr/bin/python3
"""defines mods documentation for class rectangle"""


from models.base import Base


class Rectangle(Base):
    """defines and reps a class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """this initializes a new class Rectangle"""
        super().__init__(id)

        self.validate_param(width, "width")
        self.validate_param(height, "height")
        self.validate_param(x, "x")
        self.validate_param(y, "y")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """this retrieves width oof a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """gets the width of the REctangle"""
        self.validate_param(value, "width")
        self.__width = value

    @property
    def height(self):
        """retrieves height of my drawings"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        self.validate_param(value, "height")
        self.__height = value

    @property
    def x(self):
        """retrieves x coordinates in my code"""
        return self.__x

    @x.setter
    def x(self, value):
        """gives the x coordinates"""
        self.validate_param(value, "x")
        self.__x = value

    @property
    def y(self):
        """gets the y coordinates"""
        return self.__y

    @y.setter
    def y(self, value):
        """gives the y coordinates"""
        self.validate_param(value, "y")
        self.__y = value

    def validate_param(self, param, value):
        """this validates width, height, x and y"""
        if type(param) is not int:
            raise TypeError(value + ' must be an integer')
        if param <= 0 and value in ("width", "height"):
            raise ValueError(value + " must be > 0")
        if param < 0 and value in ("x", "y"):
            raise ValueError(value + " must be >= 0")

    def area(self):
        """func returns area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """func prints the rectangle in form of # character"""
        if self.__y > 0:
            print('\n' * self.__y, end="")

        for ki in range(self.height):
            if self.__x > 0:
                print(" " * self.__x, end="")

            print("#" * self.__width)

    def __str__(self):
        """returns the str() representation of the class"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates the recs by passind the args and kwargs"""
        len_args = len(args)
        len_kwargs = len(kwargs)
        my_attributes = ["id", "width", "height", "x", "y"]

        if len_args > 5:
            len_args = 5
        if len_args > 0:
            for ki in range(len_args):
                setattr(self, my_attributes[ki], args[ki])
        elif len_kwargs > 0:
            for _key, v_value in kwargs.items():
                if _key in my_attributes:
                    setattr(self, _key, v_value)

    def to_dictionary(self):
        """returns dict representation of class rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
