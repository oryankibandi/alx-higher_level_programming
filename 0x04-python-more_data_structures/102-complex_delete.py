#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()

    keys = list(new_dict.keys())

    for i in keys:
        if new_dict[i] == value:
            a_dictionary.pop(i)

    return (a_dictionary)
