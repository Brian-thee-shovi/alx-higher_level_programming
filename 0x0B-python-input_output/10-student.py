#!/usr/bin/python3
"""mod documentation definig a class student"""


class Student():
    def __init__(self, first_name, last_name, age):
        """initialization of the class/new class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns dict representation of a student
        """
        try:
            for element_t in attrs:
                if type(element_t) is not string:
                    return self.__dict__
        except Exception:
            return self.__dict__
        the_dict = dict()
        for ky, v_value in self.__dict__.items():
            if ky in attrs:
                the_dict[ky] = v_value
        return the_dict
