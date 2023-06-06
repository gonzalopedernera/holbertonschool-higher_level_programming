#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    for i in range(0, 2):
        if i < len(tuple_a):
            a = tuple_a[i]
        else:
            a = 0
        if i < len(tuple_b):
            b = tuple_b[i]
        else:
            b = 0
        new_tuple.append(a + b)
    new_tuple = tuple(new_tuple)
    return new_tuple
