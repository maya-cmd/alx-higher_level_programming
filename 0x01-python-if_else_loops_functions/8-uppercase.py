#!/usr/bin/python3
def uppercase(str):
    for c in str:
        n = ord(c)
        if (n >= ord('a')) and (n <= ord('z')):
            c = chr(n-ord('a')+ord('A'))
        print("{}".format(c), end='')
    print()
