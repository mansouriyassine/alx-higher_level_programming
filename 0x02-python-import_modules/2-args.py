#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    print("{} {}{}{}".format(
        num_args,
        "argument" if num_args == 1 else "arguments" if num_args > 1 else "arguments.",
        ":" if num_args > 0 else ".",
        "" if num_args <= 1 else "\n"
    ))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
