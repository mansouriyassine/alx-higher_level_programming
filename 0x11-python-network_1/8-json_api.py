#!/usr/bin/python3
"""
This script sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter. It processes the response JSON
and displays the id and name if valid and not empty.
"""
import requests
import sys


if __name__ == "__main__":
    q = ""

    if len(sys.argv) > 1:
        q = sys.argv[1]

    data = {'q': q}

    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        user_data = response.json()

        if user_data:
            print("[{}] {}".format(user_data['id'], user_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
