#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        '''function: init'''
        Rectangle.__init__(self, size, size)
