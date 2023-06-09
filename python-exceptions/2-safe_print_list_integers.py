#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except ValueError:
            i += 1
            continue
        except TypeError:
            i += 1
            continue
        nb += 1
        i += 1
    print()
    return nb
