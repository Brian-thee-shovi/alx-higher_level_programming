#!/usr/bin/python3
for ram in range(0, 100):
    if ram < 99:
        print("{:02d}, ".format(ram), end='')
    else:
        print("{:02d}".format(ram))
