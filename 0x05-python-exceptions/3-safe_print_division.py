#!/usr/bin/python3
def safe_print_division(a, b):
    division_d = 0

    try:
        division_d = a / b
    except ZeroDivisionError:
        division_d = None
    finally:
        print("Inside result: {}".format(division_d))
        return division_d
