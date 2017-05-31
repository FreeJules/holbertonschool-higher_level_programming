#!/usr/bin/python3
class MyList(list):
    '''MyList class'''
    def print_sorted(self):
        '''that prints the list, but sorted (ascending sort)'''
        print (sorted(self))
