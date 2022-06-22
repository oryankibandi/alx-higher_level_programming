#!/usr/bin/python3
""" Definition of a square """


class Square:
    """
    Square class with instantiated private attribute sizes

    """
    def __init__(self, size=0):
        """
        intializes the square object

        Args:
            size (int): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        method to get the area of a square
        """
        return (self.__size ** 2)
