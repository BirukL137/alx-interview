#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""

import sys


def display_status(total_size, status_codes):
    """
    Displays the sorted status.
    """
    print(f"File size: {total_size}")
    for k, v in sorted(status_codes.items()):
        print(f"{k}: {v}")


if __name__ == "__main__":
    count = 0
    total_size = 0
    status_codes = {}

    codes = {'200', '301', '400', '401', '402', '403', '404', '405', '500'}

    try:
        for line in sys.stdin:
            count += 1
            line = line.split()
            try:
                total_size += int(line[-1])
                if line[-2] in codes:
                    try:
                        status_codes[line[-2]] += 1
                    except KeyError:
                        status_codes[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if count == 10:
                display_status(total_size, status_codes)
                count = 0
        display_status(total_size, status_codes)
    except KeyboardInterrupt as e:
        display_status(total_size, status_codes)
        raise
