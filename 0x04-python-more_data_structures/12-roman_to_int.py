#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    Rom_numeral = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    sol = 0
    previous_v = 0

    for numeral in reversed(roman_string):
        present_v = Rom_numeral.get(numeral, 0)

        if present_v >= previous_v:
            sol = sol + present_v
        else:
            sol = sol - present_v
        previous_v = present_v
    return sol
