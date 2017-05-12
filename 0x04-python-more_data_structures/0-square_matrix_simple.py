#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_mtx = []
    for row in matrix:
        row = list(map(lambda x: x**2, row))
        sqr_mtx.append(row)
    return sqr_mtx
