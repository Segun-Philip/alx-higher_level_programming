#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    if not roman_string:
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result  = 0
    get_keys = list(roman_num.keys())

    for char in roman_string:
        result += roman_num[char]
    return (result)
