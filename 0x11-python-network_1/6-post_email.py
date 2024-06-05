#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter,then finally
displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    request = requests.post(url, data=value)
    print(request.text)
