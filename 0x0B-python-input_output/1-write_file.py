#!/usr/bin/python3
"""
This module writes a string to a file
"""


def write_file(filename="", text=""):
    """
    writes text to file

    Args:
        filename (str): filename to write
        text (str): text to write
    """
    num = 0
    with open(filename, encoding='utf-8', mode='w') as a_file:
        for i in text:
            a_file.write(i)
            num += 1
    return (num)
