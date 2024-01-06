#!/usr/bin/python3
"""
This script sends a POST request to a URL with
an email parameter and displays the response body.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Your email is:", response.text)
    else:
        print("Request failed with status code:", response.status_code)
