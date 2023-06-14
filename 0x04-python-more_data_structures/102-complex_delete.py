#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_keys = []
    for g, m in a_dictionary.items():
        if m == value:
            del_keys.append(g)
    for g in del_keys:
        del a_dictionary[g]
    return a_dictionary
