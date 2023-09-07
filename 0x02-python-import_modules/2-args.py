#!/usr/bin/python3
import sys

arguments = sys.argv[1:]

num_args = len(arguments)

output = f"{num_args} argument{'s' if num_args != 1 else ''}:"
output += "" if num_args == 0 else "\n"

for i, arg in enumerate(arguments, 1):
    output += f"{i}: {arg}\n"

print(output, end="")
