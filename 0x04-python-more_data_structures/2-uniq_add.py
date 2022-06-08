#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)

    _sum = 0
    for n in new_set:
        _sum += n

    return (_sum)
