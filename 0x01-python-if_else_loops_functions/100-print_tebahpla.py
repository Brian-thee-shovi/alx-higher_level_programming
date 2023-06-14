#!/usr/bin/python3
for ram in range(122, 96, -1):
    if ram % 2 != 0:
        ram = ram - 32
    print("{}".format(chr(ram)), end="")
