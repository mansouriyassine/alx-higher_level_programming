#!/usr/bin/python3

output = ""

for number in range(100):
    if number < 99:
        output += "{:02d}, ".format(number)
    else:
        output += "{:02d}".format(number)

print(output)
