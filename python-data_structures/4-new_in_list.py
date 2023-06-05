#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx >= 0 and idx < len(my_list):
            new_list = my_list.copy()
            new_list.pop(idx)
            new_list.insert(idx, element)
            return (new_list)
    return (my_list)
