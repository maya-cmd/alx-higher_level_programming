#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    for idx in sorted(a_dictionary.keys()):
        print("{}: {}".format(idx, a_dictionary[idx]))
