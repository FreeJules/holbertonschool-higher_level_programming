#!/usr/bin/python3
class Node:

    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
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
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        return str(self.__data)


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
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
        if self.__head is None:
            return string
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data) + '\n'
            tmp = tmp.next_node
        return string[:-1]
