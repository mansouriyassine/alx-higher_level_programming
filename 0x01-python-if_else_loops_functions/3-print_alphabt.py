#!/usr/bin/python3

alphabet = ''

for letter in range(ord('a'), ord('z') + 1):
    # Append the letter to the alphabet string if it's not 'e' or 'q'
    if chr(letter) not in ('e', 'q'):
        alphabet += chr(letter)

print("{}".format(alphabet), end='')
