#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    saves json to file

    Args:
        my_obj: json object
        filename: name of file
    """
    with open(filename, mode='w', encoding='utf8') as a_file:
        a_file.write(json.dumps(my_obj))
