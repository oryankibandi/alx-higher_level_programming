#!/usr/bin/python3
"""
This returns the json representation of the string
"""
import json


def to_json_string(my_obj):
    """
    returns json
    Args:
        my_obj: object
    """
    return (json.dumps(my_obj))
