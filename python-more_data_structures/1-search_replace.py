#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    newlist.extend(my_list)
    idx = newlist.index(search)
    newlist.pop(idx)
    newlist.insert(idx, replace)
    return newlist
