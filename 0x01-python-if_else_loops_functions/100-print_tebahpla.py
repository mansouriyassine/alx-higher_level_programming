#!/usr/bin/python3

for char_code in range(ord('z'), ord('A') - 1, -1):
    char = chr(char_code)
    if char.isalpha():
        if char_code % 2 == 1:
            char = char.upper()
        print("{}".format(char), end='')

print()
