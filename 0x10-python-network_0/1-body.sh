#!/bin/bash
# This script sends a GET request to a URL passed as an argument and displays the body of the response.

curl -s -L "$1" -o /dev/null -w '%{http_code}' | grep 200 &> /dev/null && curl -s "$1"
