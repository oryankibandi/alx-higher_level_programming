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
            value (int): value to set width
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
            value (int): value to set height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """gets the area of the rectangle"""
        return (self._width * self._height)

    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return (0)
        else:
            perimeter = 2 * (self._width + self._height)
            return perimeter

    def _str__(self):
        """prints the rectangle"""
        for h in self._height:
            for w in self._width:
                print("#")
            print()
