#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        '''function: init'''
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)
