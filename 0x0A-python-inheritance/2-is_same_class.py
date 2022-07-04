#!/usr/bin/python3

"""This module chechs if the object is an instance of the class"""


def is_same_class(obj, a_class):
    """
    checks whether obj is an instance of a class

    Args:
        obj (Any): object
        a_class (class): class to check
    """
    return (type(obj) == a_class)
