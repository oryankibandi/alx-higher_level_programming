#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        pass

    new_string = my_string[:]
    i = 0

    for n in range(len(new_string)):
        if my_string[n] == 'c' or my_string[n] == 'C':
            new_string.pop(i)
        i += 1

    return (new_string)
