#!/usr/bin/python3
"""mods defining documentation for a class base"""


import json
from os import path
import csv


class Base:
    """reps class called base"""
    my_objects = 0

    def __init__(self, id=None):
        """this initializes a new class Base"""
        if id is None:
            Base.my_objects += 1
            self.id = Base.my_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this writes JSON serialization of the lis objects to a file"""
        file_name = cls.__name__ + ".json"

        with open(file_name, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            my_dict = []

            for objects in list_objs:
                my_dict.append(objects.to_dictionary())

            return f.write(cls.to_json_string(my_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns deserialization of a jso string"""
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns a class instantied from a dict of attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                my_instance = cls(8, 8)
            if cls.__name__ == "Square":
                my_instance = cls(8)
            my_instance.update(**dictionary)
            return my_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file with Json object"""
        file_name = cls.__name__ + ".json"

        if path.exists(file_name) is False:
            return []
        with open(file_name, mode="r", encoding="utf-8") as f:
            python_objs = cls.from_json_string(f.read())
            my_instances = []

            for ob_ject in python_objs:
                my_instances.append(cls.create(**ob_ject))

            return my_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """returns json serialization of the list_objects"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    rect = ["id", "width", "height", "x", "y"]
                else:
                    rect = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=rect)
                for ki in list_objs:
                    writer.writerow(ki.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """returns class instantiated from csv file"""
        my_file = cls.__name__ + ".csv"
        try:
            with open(my_file, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    rect = ["id",  "width", "height", "x", "y"]
                else:
                    rect = ["id", "size", "x", "y"]
                    my_dicts = csv.DictReader(csvfile, fieldnames=rect)
                    my_dicts = [dict([k, int(v)] for k, v in dic.items())
                                for dict_s in my_dicts]
                    return [cls.create(**dict_s) for dict_s in my_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws rects and squares using turtle module"""
        draws_turt = turtle.Turtle()
        draws_turt.screen.bgcolor("#7312c")
        draws_turt.pensize(3)
        draws_turt.shape("turtle")

        draws_turt.color("#fffff")
        for rects in list_rectangles:
            draws_turt.showturtle()
            draws_turt.up()
            draws_turt.goto(rects.x, rects.y)
            draws_turt.down()
            for ki in range(2):
                draws_turt.forward(rects.width)
                draws_turt.left(90)
                draws_turt.forward(rects.height)
                draws_turt.left(90)
            draws_turt.hideturtle()

        draws_turt.color("#b5e3d8")
        for mi_sq in list_squares:
            draws_turt.showturtle()
            draws_turt.up()
            draws_turt.goto(mi_sq, mi_sq)
            draws_turt.down()
            for ki in range(2):
                draws_turt.forward(mi_sq.width)
                draws_turt.left(90)
                draws_turt.forward(mi_sq.height)
                draws_turt(90)
            draws_turt.hideturtle()

        turtle.exitonclick
