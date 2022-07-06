#!/usr/bin/python3
"""
this module creates a Sudent class
"""

class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        This instantiates public attributes first_name, last_name and age

        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns a dictionary representation of a Student instance
        """
        return (self.__dict__.copy())
