#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    argv = sys.argv
    argc = len(argv) - 1

    print("{}{}".format(
        argc,
        " argument" + ("s:" if argc != 1 else ":") if argc > 0 else ".")
        )

    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))
