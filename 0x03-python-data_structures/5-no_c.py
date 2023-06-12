#!/usr/bin/python3

def no_c(my_string):
    other_string = ""
    for k in my_string:
        if k not in ["c", "C"]:
            other_string = other_string + k
            return other_string
