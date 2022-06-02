#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    for n in range(len(str)):
        if n != n:
            string = string + str[n]
    return (string)
