#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb = 0
    while nb <  x:
        try:
            print("{}".format(my_list[nb]), end="")
        except IndexError:
            break
        nb += 1
    print()
    return nb
