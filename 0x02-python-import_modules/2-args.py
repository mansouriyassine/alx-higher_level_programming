#!/usr/bin/python3
import sys

arguments = sys.argv[1:]

num_args = len(arguments)

print(f"{num_args} argument{'s' if num_args != 1 else ''}:", end=" ")
if num_args == 0:
    print(".")
else:
    print("")

for i, arg in enumerate(arguments, 1):
    print(f"{i}: {arg}")
