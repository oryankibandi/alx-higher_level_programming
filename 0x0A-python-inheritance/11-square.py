#!/usr/bin/python3
"""
This module creates a class square that inherits from Rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    class Square that inherits Rectangle
    """
    def __init__(self, size):
        """
        instantiates the size attribute

        Args:
            size (int): size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        returns the area of the square
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        Returns:
            returns the description of the class
        """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
