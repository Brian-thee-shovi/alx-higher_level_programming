#!/usr/bin/python3
"""defines mods for square class test cases"""
import pep8
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """testcase for class Square"""
    def test_base_pep8(self):
        """Checks the pycodestyle innit"""
        innit_checker = pep8.StyleGuide(quit=True)
        innit_report = innit_checker.check_files(['models/square.py'])
        self.assertEqual(
                innit_report.total_errors, 0,
                "Code style errors were found."
        )

        def test_getter(self):
            rect_1 = Square(9)
            self.assertEqual(rect_1.size, 9)

        def test_setter(self):
            rect_1 = Square(9)
            rect_1.size = 10
            self.assertEqual(rect_1.size, 10)

        def test_str(self):
            rect_1 = Square(4)

            with self.assertRaises(TypeError):
                rect_1.size = "Br"

        def test_negative_size(self):
            rect_1 = Square(5)

            with self.assertRaises(ValueError):
                rect_1.size = -4

        def test_zero_size(self):
            rect_1 = Square(6)

            with self.assertRaises(ValueError):
                rect_1.size = 0

        def test_decimal_size(self):
            rect_1 = Square(5)

            with self.assertRaises(TypeError):
                rect_1.size = 2.5

        def test_tuple_size(self):
            rect_1 = Square(5)

            with self.assertRaises(TypeError):
                rect_1.size = (3, 9)

        def test_empty_size(self):
            rect_1 = Square(6)

            with self.assertRaises(TypeError):
                rect_1.size = ""

        def test_none_size(self):
            rect_1 = Square(6)

            with self.assertRaises(TypeError):
                rect_1.size = None

        def test_list_size(self):
            rect_1 = Square(5)

            with self.assertRaises(TypeError):
                rect_1.size = {"re": 5, "gerr": 8}

        def test_width_size(self):
            rect_1 = Square(6)
            rect_1.size = 7
            self.assertEqual(rect_1.width, 7)
            self.assertEqual(rect_1.height, 7)

        def test_to_dict(self):
            Base._Base__my_objects = 0

            my_sq = Square(10, 2, 1, 9)
            my_sqdict = my_sq.to_dictionary()
            result = {"id": 9, "x": 2, "size": 10, "y": 1}
            self.assertEqual(my_sqdict, result)

            my_sq = Square(1, 0, 0, 9)
            my_sqdict = my_sq.to_dictionary()
            result = {"id": 9, "x": 0, "size": 1, "y": 0}
            self.assertEqual(my_sqdict, result)

            my_sq.update(6, 6, 6, 6)
            my_sqdict = my_sq.to_dictionary()
            result = {"id": 6, "x": 6, "size": 6, "y": 6}
            self.assertEqual(my_sqdict, result)


