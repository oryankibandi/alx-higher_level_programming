#!/usr/bin/python3
"""
This module appends text to file
"""


def append_write(filename="", text=""):
    """
    Appends text to file

    Args:
        filename (string): name of file
        text (string): text to append
    """
    num = 0
    with open(filename, encoding='utf-8', mode='a') as a_file:
        for i in text:
            a_file.write(i)
            num += 1

    return (num)
