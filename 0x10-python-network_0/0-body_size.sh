#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL, 
# and displays the size of the body of the response in bytes.

curl -s "$1" -o response_body -w '%{size_download}\n'
