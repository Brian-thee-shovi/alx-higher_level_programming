#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    k = list(tuple_a)
    j = list(tuple_b)

    while len(k) < 2:
        k.append(0)
    while len(j) < 2:
        j.append(0)

    k = k[:2]
    j = j[:2]
    return (k[0] + j[0], k[1] + j[1])
