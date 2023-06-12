#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_integer = my_list[0]
    for k in my_list:
        if k > max_integer:
            max_integer = k
    return max_integer
