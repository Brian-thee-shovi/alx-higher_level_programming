#!/usr/bin/python3
def magic_calculation(a, b):
    answer = 0

    for y in range(1, 3):
        try:
            if y > a:
                raise Exception("Too far")
            else:
                result += a ** b / y
        except Exception:
            answer = b + a
            break
        return answer
