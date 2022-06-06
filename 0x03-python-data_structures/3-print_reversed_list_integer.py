#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass

    reverse_list = my_list.reverse()
    for n in reverse_list:
        print("{:d}".format(n))
