#!/usr/bin/python3

if __name__ == "__main__i":

    import sys

    arguments = sys.argv[1:]

    int_args = [int(arg) for arg in arguments]

    result = sum(int_args)

    print(result)
