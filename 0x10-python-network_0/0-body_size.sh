#!/bin/bash
# This script takes a URL and displays the size of the body of the response
curl -s "$1" -o /dev/null -w '%{size_download}\n'
