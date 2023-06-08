#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        values = []
        values = list(a_dictionary.values())
        values.sort()
        for key, val in a_dictionary.items():
            if val == values[len(values) - 1]:
                return key
    return None
