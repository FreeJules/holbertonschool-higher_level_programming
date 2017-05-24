#!/usr/bin/python3
class Node:

    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("size must be an integer")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("size must be an integer")
        self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        tmp = self.__head
        if tmp is None:
            self.__head = Node(value)
        elif tmp.data > value:
            new = Node(value, tmp)
            self.__head = new
        else:
            while tmp.next_node is not None:
                if tmp.next_node.data > value:
                    break
                tmp = tmp.next_node
            new = Node(value, tmp.next_node)
            tmp.next_node = new

    def __str__(self):
        string = ''
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data) + '\n'
            tmp = tmp.next_node
        return string[:-1]