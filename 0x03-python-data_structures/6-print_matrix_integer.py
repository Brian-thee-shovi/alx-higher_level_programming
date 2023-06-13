#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)  # number of rows
    columns = len(matrix[0])  # length of rows

    if matrix == [[]]:
        print()

    for k in range(rows):
        for f in range(columns):
            if f == columns - 1:
                print("{:d}".format(matrix[k][f]))
            else:
                print("{:d}".format(matrix[k][f]), end=" ")
