#!/usr/bin/python3
"""
This script uses Basic Authentication with a personal
access token to access GitHub information and display your ID.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username>".format(sys.argv[0]))
        print("       {} <personal_access_token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    headers = {
        'Authorization': 'token {}'.format(personal_access_token)
    }

    response = requests.get('https://api.github.com/user', headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print("None")
