#!/usr/bin/python3
"""
This module prints the available attributes and methods of an objects
"""


def lookup(obj):
    """
    returns available attributes and methods of an object

    Args:
        obj: object
    """

    return dir(obj)
