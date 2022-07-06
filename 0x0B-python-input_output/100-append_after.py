#!/usr/bin/python3
"""
this module inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append a text after a substring line

    Args:
        filename: name of file
        search_string: string to search
        new_string: etxt to insert
    """

    with open(filename, 'r') as a_file:
        content = a_file.readlines()
        for (index, line) in enumerate(content):
            if line.find(search_string) != -1:
                content.insert(index+1, new_string)
        new_content = "".join(content)
    fle = open(filename, 'w')
    fle.write(new_content)
    fle.close()
