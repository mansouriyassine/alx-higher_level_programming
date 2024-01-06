#!/bin/bash
# This script sends a GET request to a URL passed as an argument and displays the body of the response.

curl -sL "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi
