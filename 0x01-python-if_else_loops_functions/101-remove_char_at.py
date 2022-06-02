#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    for k in range(len(str)):
        if k != n:
            string = string + str[k]
    return (string)
