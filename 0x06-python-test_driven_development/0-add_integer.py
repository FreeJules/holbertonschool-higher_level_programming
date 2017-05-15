#!/usr/bin/python3
'''
This is "0-add_integer" module

It supplies one function, add_integer(a, b)

For example:
>>> add_integer(100, -2)
98
'''


def add_integer(a, b):
    """
    Return the addition of two numbers
    The numbers can be integers or floats
    If they are floats they get casted to integers first

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "test")
    b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (float, int)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
