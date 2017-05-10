#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    aList = list(tuple_a)
    bList = list(tuple_b)
    for i in range(2):
        aList.append(0)
        bList.append(0)
    sum_0 = aList[0] + bList[0]
    sum_1 = aList[1] + bList[1]
    tuple_c = (sum_0, sum_1)
    return tuple_c
