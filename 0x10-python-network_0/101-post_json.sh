#!/bin/bash
# This script sends a json post  reuqest to a URL passed as the first argument
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
