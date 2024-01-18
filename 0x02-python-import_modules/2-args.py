#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    number_args = len(argv) - 1

    if number_args == 0:
        print("Number of arguments is 0.")
    elif number_args == 1:
        print("Number of arguments is 1:")
    else:
        print(f"{number_args} arguments are present:")

    for i in range(number_args):
        print(f"{i + 1}: {argv[i + 1]}")
