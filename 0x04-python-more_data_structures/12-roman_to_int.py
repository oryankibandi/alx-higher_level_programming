#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if (roman_string is None or type(roman_string) is not str):
        return (0)

    int_val = 0
    dummy_val = 0

    for i in roman_string:
        if rom_val[i] <= dummy_val:
            int_val += rom_val[i]
        else:
            int_val = rom_val[i] - (dummy_val * 2)
        dummy_val = rom_val[i]

    return (int_val)
