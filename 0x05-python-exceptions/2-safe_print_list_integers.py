#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0

    for index in range(0, x + 1):
        try:
            if i == x:
                print("{:d}".format(my_list[index]))
                i += 1
            else:
                print("{:d}".format(my_list[index]), end='')
                i += 1
        except ValueError:
            i += 1
        except IndexError:
            raise(IndexError)

    return (i)
