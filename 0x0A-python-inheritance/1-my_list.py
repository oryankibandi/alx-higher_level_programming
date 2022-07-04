#!/usr/bin/python3
"""
This module creates a class MyList that inherits frm `list`
"""


class MyList(list):
    """
    MyList class
    """
    def print_sorted(self):
        """
        prints a sorted list of class attributes
        """

        print(sorted(self))
