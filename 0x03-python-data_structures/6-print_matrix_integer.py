#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    numrows = len(matrix)
    numcols = len(matrix[0])
    for i in range(0, numrows):
        for j in range(0, numcols):
            if j == numcols - 1:
                print('{:d}'.format(matrix[i][j]), end='')
            else:
                print('{:d}'.format(matrix[i][j]), end=' ')
        print()
