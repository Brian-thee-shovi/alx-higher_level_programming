#!/usr/bin/python3
"""Defines an inherited list"""


class MyList(list):
    """defines sorted supperclass list"""

    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
