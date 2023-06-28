#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for ki in range(x):
            print(my_list[ki], end="")
    except IndexError:
        x = ki
    finally:
        print()
        return x
