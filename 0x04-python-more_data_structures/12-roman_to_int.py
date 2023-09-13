#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    for char in roman_string[::-1]:
        if roman_dict[char] >= prev_value:
            result += roman_dict[char]
        else:
            result -= roman_dict[char]
        prev_value = roman_dict[char]

    return result
