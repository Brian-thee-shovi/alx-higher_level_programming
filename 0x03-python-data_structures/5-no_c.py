#!/usr/bin/python3

def no_c(my_string):
    other_string = ""
    for k in my_string:
        if k.lower() != 'c':
            other_string += k
    return other_string
