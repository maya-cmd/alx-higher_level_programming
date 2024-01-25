#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    max_val = 0
    max_key = None

    for key, val in a_dictionary.items():
        if val > max_val:
            max_key = key
            max_val = val
    return max_key
