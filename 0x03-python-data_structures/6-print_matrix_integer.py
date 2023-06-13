#!usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for k in range(len(matrix)):
        for h in range(len(matrix[k])):
            if h == len(matrix[k]) - 1:
                print("{:d}".format(matrix[k][h]), end='')
            else:
                print("{:d}".format(matrix[k][h]), end=' ')
        print()
