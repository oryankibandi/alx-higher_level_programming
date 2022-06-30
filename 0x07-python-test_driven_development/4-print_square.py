#!/usr/bin/python3
"""
This module prints a square with # symbol
"""


def print_square(size):
    """
    prints size of a square with the symbol #

    Args:
        size: size of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for h in range(0, size):
        for w in range(0, size):
            print("#", end='')
        print()
