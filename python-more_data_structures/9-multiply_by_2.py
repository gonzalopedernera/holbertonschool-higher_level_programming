#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = {}
    newdic.update(a_dictionary)
    keys = list(newdic)
    for i in keys:
        newdic[i] *= 2
    return newdic
