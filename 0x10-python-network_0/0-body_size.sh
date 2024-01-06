#!/bin/bash
# Script to fetch the content length from a URL's response headers

curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
