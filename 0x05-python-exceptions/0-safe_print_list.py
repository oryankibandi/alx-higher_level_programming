#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0

    for item in my_list:
        if i > x:
            break
        try:
            if i < x:
                print(item, end='')
                i += 1
            elif i == x:
                print(item)
                i += 1
        except (RuntimeError, TypeError, NameError) as err:
            print(f"Unexpected {err=}, {type(err)=}")

    return (i)
