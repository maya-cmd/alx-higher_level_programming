#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for i in range(x):
            print(f"{my_list[i]}", end="")
            counter += 1
        print()
        return counter
    except IndexError:
        print()
        return counter
