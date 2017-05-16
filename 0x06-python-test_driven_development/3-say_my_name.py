#!/usr/bin/python3
'''
This is "3-say_my_name" module

It supplies one function, say_my_name(first_name, last_name="")

For example:
>>> say_my_name("Julija", "Lee")
My name is Julija Lee
'''


def say_my_name(first_name, last_name=""):
    """
    prints "My name is first_name last_name"
    first_name and last_name must be strings
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    new_str = 'My name is ' + first_name + " " + last_name
    print(new_str)
