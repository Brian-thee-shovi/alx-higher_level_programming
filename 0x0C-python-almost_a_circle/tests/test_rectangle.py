#!/usr/bin/python3
"""defines mods documentation for testing the rectangle class"""
import pep8
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """class defining the Rectangle test"""

    def test_pep8_Rectangle(self):
        innit_checker = pep8.StyleGuide(quit=True)
        innit_report = innit_checker.check_files(['models/rectangle.py'])
        self.assertEqual(
                innit_report.total_errors, 0,
                "code style errors were found."
        )

    def test_subcls_rectangle(self):
        """
        tests functionality of the subclass rect
        reigarding the superclass Base
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_args(self):
        """tests parameters of rectangle class"""
        rect_1 = Rectangle(10, 2)
        rect_2 = Rectangle(2, 10)
        rect_3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(rect_1.id, 1)
        self.assertEqual(rect_1.width, 10)
        self.assertEqual(rect_1.height, 2)
        self.assertEqual(rect_1.x, 0)
        self.assertEqual(rect_1.y, 0)
        self.assertEqual(rect_2.id, 4)
        self.assertEqual(rect_2.width, 2)
        self.assertEqual(rect_2.height, 10)
        self.assertEqual(rect_2.x, 0)
        self.assertEqual(rect_2.y, 0)
        self.assertEqual(rect_3.id, 12)
        self.assertEqual(rect_3.width, 10)
        self.assertEqual(rect_3.height, 2)
        self.assertEqual(rect_3.x, 0)
        self.assertEqual(rect_3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_str_param(self):
        """string parameters of the Rectangle class"""
        with self.assertRaises(TypeError):
            Rectangle("Brian", "python")

    def test_paramtypes(self):
        """tests class rectangle for types of parameters"""
        with self.assertRaises(TypeError):
            Rectangle(2.06, 3)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-543345543, 45)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle('', 8)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(8, 34.67)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(10, "Brian")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(9, True)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(4, -44553483598)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(6, 3, 1.25)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(7, 9, "Brian")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(6, 10, True)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(10, 15, -5834394523)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(6, 8, 5, "brian")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(6, 8, True)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(6, 8, 6, -448345868)
            raise ValueError()
