#!/usr/bin/python3
"""
This script sends a POST request to a URL with
an email parameter and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Your email is:", response.text)
    else:
        print("Request failed with status code:", response.status_code)