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

    def to_json(self, attr=None):
        """
        returns a dictionary representation of a Student instance
        """
        is_str = True
        att_copy = self.__dict__.copy()
        new_att = {}
        for i in attr:
            if type(i) is not str:
                is_str = False
        if is_str:
            for i in attr:
                new_att[i] = att_copy[i]
            return (new_att);
        else:
            return (att_copy)
