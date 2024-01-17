#!/usr/bin/python3

def print_last_digit(num):
    if num < 0:
        last_dig = abs(num) % 10
        print(f"{last_dig}", end="")
        return last_dig
    else:
        last_dig = num % 10
        print(f"{last_dig}", end="")
        return last_dig
