#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        '''function: init'''
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)
        self.__width = size
        self.__height = size

    def __str__(self):
        '''string representation'''
        s = "[{}] {}/{}".format(self.__class__.__name__,
                                self.__width, self.__height)
        return s
