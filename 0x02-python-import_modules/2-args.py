#!/usr/bin/python3

if __name__ == "__main__":
    """Print the count and list of command-line arguments."""
    import sys

    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("No arguments provided.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    for index, argument in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(index, argument))
