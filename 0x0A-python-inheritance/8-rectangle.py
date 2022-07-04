#!/usr/bin/python3
"""
This module inherits from BaseGeoetry class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle inherits from class BaseGeometry
    """
    def __init__(self, width, height):
        """
        initializes height and width

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
