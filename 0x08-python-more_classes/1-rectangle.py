#!/usr/bin/python3
"""Empty class that defines a class Rectangle"""


class Rectangle:
    """This is a Rectangle class"""
    def __init__(self, width=0, height=0):
        """
        method called when initializing an instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self._width = width
        self._height = height

    @property
    def width(self):
        """"retrieves the width attribute"""
        return (self._width)

    @property
    def height(self):
        """getter for the height attribute"""
        return (self._height)

    @width.setter
    def width(self, value):
        """
        setter method for the width attribute

        Args:
            value (int): value to set the width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @height.setter
    def height(self, value):
        """
        setter method for the height attribute

        Args:
            value (int):value to set the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
