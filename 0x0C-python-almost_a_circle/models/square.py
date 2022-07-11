#!/usr/bin/python3
"""
This module ontains the Square class that inherits from Retangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes attributes of the class

        Args:
            size (int): size of the square
            x (int): x
            y (int): y
            id (int): id
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns string representation of the instance
        """
        return ("[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """
        getter for the size attribute
        """
        return (self.size)

    @size.setter
    def size(self, value):
        """
        setter for the size attribute
        """
        self.size = value
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        updates attributes

        Args:
            args: list of arguments
            kwargs: dictionary of arguments
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returs a new dictionary representation
        """
        new_dict = {"id": self.id, "x": self.__x,
                    "size": self.size, "y": self.__y}
        return (new_dict)
