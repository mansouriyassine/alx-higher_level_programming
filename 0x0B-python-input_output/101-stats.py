#!/usr/bin/python3
import sys


def print_metrics(file_size, status_codes):
    print("File size: {:d}".format(file_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{:s}: {:d}".format(code, status_codes[code]))

file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        split_line = line.split()
        try:
            file_size += int(split_line[-1])
            status_code = split_line[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (ValueError, IndexError):
            pass
        if line_count == 10:
            print_metrics(file_size, status_codes)
            line_count = 0

except KeyboardInterrupt:
    pass

print_metrics(file_size, status_codes)
