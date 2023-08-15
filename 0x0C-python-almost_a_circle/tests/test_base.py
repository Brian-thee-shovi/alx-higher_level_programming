#!/usr/bin/python3
"""
defines mods documentation for implementing a unittest to the BASE class
"""
import os
import pep8
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """tests instantiation of the Base class"""

    def test_pep8_compliance(self):
        """this tests pycodestyle"""
        innit_checker = pep8.StyleGuide(quit=True)
        innit_report = innit_checker.check_files(['models/base.py'])
        self.assertEqual(
            innit_report.total_errors, 0,
            "Code style errors were found."
        )

        def test_positive_id(self):
            """tests for positive id of the base class"""
            mybase_instance = Base(54)
            self.assertEqual(mybase_instance.id, 54)
            mybase_instance = Base(75)
            self.assertEqual(mybase_instance.id, 75)

        def test_negative_id(self):
            """this tests for negative id of the base class"""
            mybase_instance = Base(-32)
            self.assertEqual(mybase_instance.id, -32)
            mybase_instance = Base(-13)
            self.assertEqual(mybase_instance.id, -13)

        def test_no_id(self):
            """this test for a none id"""
            mybase_instance = Base(None)
            self.assertEqual(mybase_instance.id, 2)

        def test_str_id(self):
            mybase_instance = Base("Brian shovi")
            self.assertEqual(mybase_instance.id, "Brian shovi")
            mybase_instance = Base("am innit")
            self.assertEqual(mybase_instance.id, "am innit")

        def test_to_json_str(self):
            """json string func being tested"""
            rect_instance = Rectangle(16, 10, 4, 9, 45)
            my_data = rect_instance.to_dictionary()
            json_data = Base.to_json_string([my_data])
            self.assertEqual(type(json_data), str)

        def test_to_json_str_emptyarg(self):
            """tests if list_dictionaries is empty"""
            my_emptylist = []
            json_data = Base.to_json_string(my_emptylist)
            self.assertEqual(json_data, "[]")

            None_list = None
            json_data = Base.to_json_string(None_list)
            self.assertEqual(json_data, "[]")

        def test_base_instance(self):
            """checks for a base instance"""
            mybase_instance = Base()
            self.assertEqual(type(mybase_instance), Base)
            self.assertTrue(isinstance(mybase_instance, Base))

        def test_to_json_str_normal_working(self):
            """tests working of the json function"""
            my_dict = {'id': 23, 'x': 24, 'y': 21, 'width': 10, 'height': 8}
            json_dict = Base.to_json_string([my_dict])

            self.assertTrue(isinstance(my_dict, dict))
            self.assertTrue(isinstance(json_dict, str))
            self.assertCountEqual(
                    json_dict,
                    '{["id": 23, "x": 24, "y": 21, "width": 10, "height": 8]}'
                    )

        def test_to_json_str_wrong_working(self):
            """test if the json func is working correctly"""
            json_data = Base.to_json_string(None)
            self.assertEqual(json_data, "[]")

            error = ("to_json_string() missing 1 required positional argument: " + "'list_dictionaries'")

            with self.assertRaises(TypeError) as error_mesg:
                Base.to_json_string()

            self.assertEqual(error, str(error_mesg.exception))

            err = "to_json_string() takes 1 positional argument but 2 were given"
            with self.assertRaises(TypeError) as error_mesg:
                Base.to_json_string([{24, 56}], [{32, 12}])

            self.assertEqual(err, str(error_mesg.exception))

        def test_save_to_file_wrongly(self):
            """tests the functionality of the save to file func"""
            with self.assertRaises(AttributeError) as error_mesg:
                Base.save_to_file([Base(1), Base(2)])

            self.assertEqual(
                    "'Base' object has no attribute 'to_dictionary'",
                    str(error_mesg.exception)
            )

        def test_load_from_file(self):
            """this tests the deserialization"""
            if os.path.exists("Base.json"):
                os.remove("Base.json")

            if os.path.exists("Rectangle.json"):
                os.remove("Rectangle.json")

            if os.path.exists("Square.json"):
                os.remove("Square.json")

            my_rectresult = Rectangle.load_from_file()
            self.assertEqual(my_result, [])

            my_sqresult = Square.load_from_file()
            self.assertEqual(my_sqresult, [])

            err = "load_from_file() takes 1 positionall argument but 2 were given"
            with self.assertRaises(TypeError) as error_mesg:
                Rectangle.load_from_file('Brian shovi')

            self.assertEqual(err, str(error_mesg.exception))

        def test_create_args_kwargs(self):
            """this tests the create method"""
            with self.assertRaises(TypeError) as error_mesg:
                err = Rectangle.create('Brian shovi')

            self.assertEqual(
                "create() takes 1 positional argument but 2 were given",
                str(error_mesg.exception)
            )




