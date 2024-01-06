#!/usr/bin/python3
# Fetches a URL using urllib and prints the body response
import urllib.request


if __name__ == "__main__":
    # URL to be fetched
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        response_content = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(response_content)))
        print("\t- content: {}".format(response_content))
        print("\t- utf8 content: {}".format(response_content.decode("utf-8")))
