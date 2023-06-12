#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_line = []
    for k in my_list:
        if k % 2 == 0:
            new_line.append(True)
        else:
            new_line.append(False)
    return new_line
