#!/usr/bin/python3
class MyInt(int):
    '''rebel int class'''
    def __eq__(self, other):
        '''if true returns false'''
        return False

    def __ne__(self, other):
        '''if false returns ture'''
        return True
