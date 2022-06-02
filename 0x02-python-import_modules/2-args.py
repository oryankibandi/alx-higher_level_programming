#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg_len = sys.argv - 1
    i = 0

    if arg_len == 0:
        print("{} arguments.".format(arg_len))
    elif arg_len == 1:
        print("{} argument:".format(arg_len))
    else:
        print("{} arguments:".format(arg_len))

    if arg_len >= 1:
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, sys.argv[i]))
                i += 1

