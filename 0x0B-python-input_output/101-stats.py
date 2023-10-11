#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_metrics(file_size, status_codes):
    """Print accumulated metrics.

    Args:
        file_size (int): The accumulated file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("Total file size: {}".format(file_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_metrics(file_size, status_codes)
                line_count = 1
            else:
                line_count += 1

            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_metrics(file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)
        raise
