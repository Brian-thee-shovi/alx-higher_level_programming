#!/usr/bin/python3
"""mods documentation defining a class student"""


class Student():
    def __init__(self, first_name, last_name, age):
        """initialises a class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns dict representation of student
        """
        try:
            for element_t in attrs:
                if type(element_t) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        d_dict = dict()
        for ky, v_value in self.__dict__items():
            if ky in attrs:
                d_dict[ky] = v_value
        return d_dict

    def reload_from_json(self, json):
        """
        replaces all attriutes of student instance
        """
        for ky, v_value in json.items():
            if ky in self.__dict__:
                self.__dict__[ky] = v_value
