#!/usr/bin/python3
for digit in range(0, 99):
    if digit % 10 > num / 10:
        if digit != 89:
                print("{:02d}, ".format(digit), end='')
        else:
                print("{:02d}".format(digit))
