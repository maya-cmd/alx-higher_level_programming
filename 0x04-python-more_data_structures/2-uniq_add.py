#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_num = set()
    total_count = 0

    for number in my_list:
        if number not in unique_num:
            unique_num.add(number)
            total_count += number

    return total_count
