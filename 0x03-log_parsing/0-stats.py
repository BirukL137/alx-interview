#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""

import sys


if __name__ == "__main__":
    codes = {'200: 0', '301: 0', '400: 0', '401: 0', '402: 0', '403: 0',
             '404: 0', '405: 0', '500: 0'}
    count = 1
    total_size = 0

    def display():
        """
        A method that displays sorted status.
        """
        print(f"File size: {total_size}")
        for k in sorted(codes.keys()):
            if codes[k]:
                print(f"{k}: {codes[k]}")


    def parse(line):
        """ Read, parse and grab data"""
        try:
            parsed_line = line.split()
            status_code = parsed_line[-2]
            if status_code in codes.keys():
                codes[status_code] += 1
            return int(parsed_line[-1])
        except Exception:
            return 0

    try:
        for i in sys.stdin:
            total_size += parse(i)
            if count % 10 == 0:
                display()
            count += 1
    except KeyboardInterrupt:
        display()
        raise
    display()
