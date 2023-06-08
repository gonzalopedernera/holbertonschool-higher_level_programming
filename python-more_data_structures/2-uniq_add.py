#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    values = set(my_list)
    for i in values:
        res += i
    return res
