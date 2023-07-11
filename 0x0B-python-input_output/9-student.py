#!/usr/bin/python3
"""mods documentation representing a student"""


class Student():
    """reps the class student"""
    def __init__(self, first_name, last_name, age):
        """initializes the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dic representation of a student"""
        return self.__dict__
