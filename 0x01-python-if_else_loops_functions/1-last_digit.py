#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
L_digit = abs(number) % 10
if number < 0:
    L_digit = -L_digit
        print("Last digit of {} is {} and is ".format(number, L_digit), end="")
    if L_digit > 5:
        print("greater than 5")
    elif L_digit == 0:
        print("0")
    else:
        print("less than 6 and not 0")
