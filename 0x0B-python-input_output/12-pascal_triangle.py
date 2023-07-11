#!/usr/bin/python3
"""mods documentation defining pascals triangle func"""


def pascal_triangle(n):
    """
    pascal triangle returns a list of integers
    representing the triangle
    """

    if n <= 0:
        return []
    t_triangle = [[1]]
    for ki in range(1, n):
        row = [1]
        l_row = t_triangle[ki - 1]
        for j in range(1, ki):
            row.append(l_row[j - 1] + l_row[j])
        row.append(1)
        t_triangle.append(row)
    return t_triangle
