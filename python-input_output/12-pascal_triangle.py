#!/usr/bin/python3
"""Returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s
    triangle of n
    Args:
        n: an int
    """
    p_t = [[]]
    if n <= 0:
        return p_t
    else:
        p_t = [[1]]
        sub_list = [1]
        old_list = []
        k = 0
        for i in range(0, n):
            for j in range(0, i):
                if j == i - 1:
                    sub_list.append(1)
                else:
                    sub_list.append(old_list[j + 1] + old_list[j])
            if i != 0:
                p_t.append(sub_list)
            old_list = list(sub_list)
            sub_list = [1]
    return p_t
