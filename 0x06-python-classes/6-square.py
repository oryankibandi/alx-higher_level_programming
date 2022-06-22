#!/usr/bin/python3
""" Definition of a square """


class Square:
    """
    Square class with instantiated private attribute sizes

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        intializes the square object

        Args:
            size (int): Size of the square

            position (tuple): Deefines position of the square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        method to get the area of a square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """returns the size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        sets the __size attribute

        Args:
            value (int):value to set size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """prints size of the square with #"""
        if self.__size == 0:
            print()
        else:
            for h in range(self.__size):
                print("#" * self.__size)

    @property
    def position(self):
        """getter method for position attribute"""
        return self._position

    @position.setter
    def position(self, value):
        """
        sets the position attribute

        Args:
            value (tuple): position of the square
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
