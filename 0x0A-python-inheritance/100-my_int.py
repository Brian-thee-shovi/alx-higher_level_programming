#!/usr/bin/python3
"""defines mods documentation"""


class MyInt(int):
    """class reps the subclass MyInt"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
