#!/usr/bin/python3
"""
This script sends a request to a URL and displays the
value of the 'X-Request-Id' variable in the response header.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code == 200:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id not found in response headers.")
    else:
        print("Request failed with status code:", response.status_code)
