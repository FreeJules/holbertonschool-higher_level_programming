#!/usr/bin/python3
'''
This is "2-matrix_divided.py" module

It supplies one function, matrix_divided(matrix, div)

For example:
>>> matrix = [[1, 2, 3],[4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
'''


def matrix_divided(matrix, div):
    """
    Return the matrix divided by div
    Matrix must be a list of lists of integers or floats
    Each row of the matrix must be of the same size
    div must be a number (integer or float) and non-zero
    All elements of the matrix should be divided by div, rounded to 2 decimals

    >>> matrix_divided(matrix, 1.5)
    [[0.67, 1.33, 2.0], [2.67, 3.33, 4.0]]
    >>> matrix_divided(matrix, 0)
    ZeroDivisionError: division by zero
    >>> matrix = [[1, 2, 3],[4, 6]]
    >>> matrix_divided(matrix, 2)
    TypeError: Each row of the matrix must have the same size
    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_mtx = []
    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists)'
                                ' of integers/floats')
    cols = len(matrix[0])
    for row in matrix:
        if len(row) != cols:
            raise TypeError('Each row of the matrix must have the same size')
        row = list(map(lambda x: round(x/div, 2), row))
        new_mtx.append(row)
    return(new_mtx)
