#!/usr/bin/python3

"""Finds the peak in a list of integers"""


def find_peak(list_of_integers):
    if len(list_of_integers) == 0 or list_of_integers is None:
        return None

    top = len(list_of_integers)
    bottom = 0
    mid = int((top - bottom) / 2)

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if len(list_of_integers) == 1:
        return max(list_of_integers)

    if list_of_integers[mid] >= list_of_integers[mid + 1]
    and list_of_integers[mid] >= list_of_integers[mid - 1]:
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
