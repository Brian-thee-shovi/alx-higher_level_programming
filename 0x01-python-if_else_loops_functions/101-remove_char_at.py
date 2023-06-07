#!/usr/bin/python3
def remove_char_at(str, n):
    newstring = ""
    for ram in range(len(str)):
        if ram != n:
            newstring = newstring + str[ram]
            return newstring
