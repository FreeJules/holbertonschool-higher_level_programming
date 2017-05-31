#!/usr/bin/python3
class BaseGeometry:
    '''class BaseGeometry'''
    def area(self):
        '''area function'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''integer validator'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''class Rectangle; inherits from BaseGeometry'''
    def __init__(self, width, height):
        '''init function'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
