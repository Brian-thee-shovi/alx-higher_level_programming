#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    for ram in str:
        if ord(ram) >= 97 and ord(ram) <= 122:
            str_upper = str_upper + chr(ord(ram) - 32)
        else:
            str_upper = str_upper + ram
            print("{}".format(str_upper))
