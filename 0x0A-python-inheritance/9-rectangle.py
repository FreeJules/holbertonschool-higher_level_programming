#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle; inherits from BaseGeometry'''
    def __init__(self, width, height):
        '''init function'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''area function'''
        return self.__width * self.__height

    def __str__(self):
        '''string representation function'''
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string
