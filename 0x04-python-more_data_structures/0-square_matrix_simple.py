#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    solution = [[num**2 for num in row] for row in matrix]
    return solution
