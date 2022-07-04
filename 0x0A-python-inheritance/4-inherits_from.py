#!/usr/bin/python3
"""
This module checks if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited
    from the specified class ; otherwise False

    Args:
        obj: object
        a_class: class to check
    """

    return (type(obj) != a_class and issubclass(type(obj), a_class))
