#!usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)  # number of rows
    columns = len(matrix[0])  # length of rows

    if matrix == [[]]:
        print()

    for r in range(rows):
        for c in range(columns):
            if c == columns - 1:
                print("{:d}".format(matrix[r][c]))
            else:
                print("{:d}".format(matrix[r][c]), end=" ")
