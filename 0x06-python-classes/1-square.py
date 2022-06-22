#!/usr/bin/python3
"""
This module initilizes the private attribute size
"""


class Square:
    """ square class """
    def __init__(self, size):
        """
        initializes the size attribute

        Args:
            size (int): size to set
        """
        self.__size = size
