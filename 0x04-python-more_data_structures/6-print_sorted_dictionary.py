#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dic = sorted(a_dictionary)
    for h in dic:
        print(h + ":", a_dictionary[h])
