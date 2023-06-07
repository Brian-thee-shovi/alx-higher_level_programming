#!/usr/bin/python3
def fizzbuzz():
    for ram in range(1, 101):
        if ram % 3 == 0 and ram % 5 == 0:
            print("FizzBuzz", end=' ')
        elif ram % 3 == 0:
            print("Fizz", end=' ')
        elif ram % 5 == 0:
            print("Buzz", end=' ')
        else:
            print("{:d}".format(ram), end=' ')
