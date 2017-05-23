#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 positive "
                                "integers")
        self.__position = value

    def area(self):
        return int(self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__size + self.__position[1]):
            if i < self.__position[1]:
                print()
                continue
            for j in range(0, self.__size + self.__position[0]):
                if j < self.__position[0]:
                    print(' ', end='')
                    continue
                print('#', end='')
            print()
