#!/usr/bin/python3
"""
This module adds two integers
"""


def add_integer(a, b=98):
    """
    returns sum of the two integers

    Args:
        a (int): First integer
        b (int): Second integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(a) == float:
        a = int(a)

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif type(b) == float:
        b = int(b)

    return (a + b)

