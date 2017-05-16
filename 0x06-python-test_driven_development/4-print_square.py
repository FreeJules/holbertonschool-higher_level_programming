#!/usr/bin/python3
'''
This is "4-print_square" module

It supplies one function, print_square(size)

For example:
>>> print_square(2)
##
##

'''


def print_square(size):
    """
    Prints a square with the character #
    Size must be an integer and greater than or equal to 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size < 0 and isinstance(size, float):
        raise TypeError('size must be an integer')
    for row in range(0, size):
        for item in range(0, size):
            print('#', end='')
        print()
