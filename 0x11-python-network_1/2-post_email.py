#!/usr/bin/python3
"""
This script takes in a URL and an email
sends a POST request to the URL with the email as a parameter
and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')  # data should be bytes

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        # Read and decode the response body
        response_body = response.read().decode('utf-8')

        print(response_body)
