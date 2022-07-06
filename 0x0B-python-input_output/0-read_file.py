#!/usr/bin/python3
"""
This module prints the contents of a text file
"""


def read_file(filename=""):
    """
    reads the file and pints to standard output

    Args:
        filename (str):name of file
    """
    with open('filename', encoding='utf-8') as a_file:
        print(a_file.read())
