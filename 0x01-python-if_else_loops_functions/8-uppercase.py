#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase using ord() and chr() functions
            uppercase_char = chr(ord(char) - 32)
            print(uppercase_char, end='')
        else:
            print(char, end='')
    print()
