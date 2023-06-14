#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    other_dict = {}
    for key, f in a_dictionary.items():
        other_dict[key] = f * 2
    return other_dict
