#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) == str and roman_string is not None:
        res = 0
        for i in range(0, len(roman_string)):
            currval = values.get(roman_string[i])
            res += currval
            if i > 0:
                prevval = values.get(roman_string[i - 1])
                if prevval < currval:
                    res -= prevval * 2
        return res
    else:
        return 0
