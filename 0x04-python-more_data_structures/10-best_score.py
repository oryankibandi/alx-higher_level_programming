#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    keys = list(a_dictionary.keys())
    largest_key = ""
    value = 0

    for i in keys:
        if a_dictionary[i] > value:
            value = a_dictionary[i]
            largest_key = i

    return (largest_key)
