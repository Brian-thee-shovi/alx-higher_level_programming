#!/usr/bin/python3
"""
Module showing division the elements of  a matrix
"""


def matrix_divided(matrix, div):
    """
    funcs dividing all elements of a matrix
    """
    matri_x = []
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(error)
    if type(div) is int or type(div) is float or type(div) is None:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        lengt_h = len(matrix[0])
    else:
        raise TypeError(error)
    for ki in range(len(matrix)):
        if len(matrix[w]) is not lengt_h:
            raise TypeError("Each row of the matrix must have the same size")
        matri_x.append([])
        for m in matrix[ki]:
            if type(m) is int or type(m) is float:
                matri_x[ki].append(round(m / div, 2))
            else:
                raise TypeError(error)
    return matri_x
