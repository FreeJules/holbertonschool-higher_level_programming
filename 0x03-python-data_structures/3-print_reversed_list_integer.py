#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        if len(my_list) > 0:
            l = len(my_list) - 1
            for i in my_list:
                print('{:d}'.format(my_list[l]))
                l -= 1
