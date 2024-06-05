#!/usr/bin/python3
"""
Takes and sends request to the URL, then displays the
values to the X-Request-d variable located in the header
reesponse
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header['X-Request-Id'])
