#!/usr/bin/python3
"""
This module is the base class for all our other classes
"""


import json

class Base:
    """
    class Base
    """
    __nb__objects = 0

    def __init__(self, id=None):
        """
        initializes private and public attributes

        id (int): Id attribute
        """
        if id is None:
            self.__nb__objects += 1
            self.id =self.__nb__objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON representation of the list

        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string representatin of list_objs to a file

        Args:
            list_objs: list of instances
        """
        if list_objs is None or len(list_objs) == 0:
            objstr = "[]"
        else:
            objstr = cls.to_json_string([o.to_dictionary() for o in list_objs])

        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as a_file:
            a_file.write(objstr)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string

        Args:
            json_string:  a string representing a list of dictionaries
        """
        js_list = []
        if json_string is Not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            js_list = json.loads(json_string)
        return js_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes.
        Args:
            dictionary (**kwargs): used as **kwargs
        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""

        filename = cls.__name__ + ".json"
        l = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    l.append(cls.create(**d))
        return l
