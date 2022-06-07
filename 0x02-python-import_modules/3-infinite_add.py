#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    length = len(sys.argv)
    res = 0
    for arg in range(1, length):
        res += int(sys.argv[arg])
    print("{:d}".format(res))
