#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}

    output = 0
    old_value = 0

    for char in reversed(roman_string):
        old_value = roman_nums[char]

        output += old_value if output < old_value * 5 else - old_value

    return output
