#!/usr/bin/python3
"""
This module contains the Rectangle class which inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes attriutes

        width: width of the rectangle
        height: height of the rectangle
        x (int): x position
        y (int): y position
        id (int): id atribute of parent class
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        returns the attribute
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        sets the attribute to the provided value
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        returns the attribute
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        sets the attribute to the provided value
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        returns the attribute
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        sets the attribute to the provided value
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        returns the attribute
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        sets the attribute to the provided value
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This method returns area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for m in range(0, self.__y):
            print()
        for h in range(0, self.__height):
            for n in range(0, self.__x):
                print(" ", end='')
            for w in range(0, self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """
        overrides the __str__ method
        """
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
        return (string)

    def update(self, *args, **kwargs):
        """
        updates the Rectangle with the new attributes

        Args:
            args []: List of arguments
        """
        if args is not None and len(args) != 0:
            att_num = 1
            for att in args:
                if att_num == 1:
                    self.id = att
                elif att_num == 2:
                    self.__width = att
                elif att_num == 3:
                    self.__height = att
                elif att_num == 4:
                    self.__x = att
                else:
                    self.__y = att
                att_num += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.__id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        returns a dictionary represnetation
        """
        new_dict = {"x": self.__x, "y": self.__y, "id": self.id,
                    "height": self.__height, "width": self.__width}
        return (new_dict)
