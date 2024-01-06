#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response
f an HTTP error occurs, it catches the exception
and prints
the error code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
