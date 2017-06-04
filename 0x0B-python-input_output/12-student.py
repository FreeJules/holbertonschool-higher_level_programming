#!/usr/bin/python3
class Student():
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """init method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json"""
        d = {}
        if attrs is not None and type(attrs) is list:
            for i in attrs:
                if type(i) is str:
                    if hasattr(self, i):
                        value = getattr(self, i)
                        d[i] = value
            return d
        return self.__dict__
