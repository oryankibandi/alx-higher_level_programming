#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0

    for index in range(0, x + 1):
        try:
            if i == x:
                print("{:d}".format(my_list[index]))
            else:
                print("{:d}".format(my_list[index]), end='')
        except (ValueError, TypeError)
            pass
        else:
            i += 1

    return (i)
