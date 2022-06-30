#!/usr/bin/python3
"""
This module prints a text and a new line after the characters `.` `?` and `:`
"""


def text_indentation(text):
    """
    Prints a string and a new line after the characters `.` `?` and `:`

    Args:
        text:Text to print
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    list_text = list(text)
    del_space = False

    for i in list_text:
        if i == '.' or i == '?' or i == ':':
            print(i, end='')
            print()
            print()
            del_space = True
        else:
            if del_space:
                if i == ' ':
                    del_space = False    
                else:
                    print(i, end='')
                    del_space = False
            else:
                print(i, end='')


