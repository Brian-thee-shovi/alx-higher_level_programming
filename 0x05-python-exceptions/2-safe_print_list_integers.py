#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_element = 0
    for ki in range(x):
        try:
            print("{:d}".format(my_list[ki]), end="")
            num_element += 1
        except(ValueError, TypeError):
            pass
        print()
        return num_element
