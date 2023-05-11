#!/usr/bin/env python3
"""
A script that reads stdin line by line and computes metrics.
"""

import sys

#       27.59.104.166 - - [04/Oct/2019:21:15:54 +0000] "GET /users/login HTTP/1.1" 200 41716 "-" "okhttp/3.12.1"
#       IP_ADDRESS - -    [DATETIME]                   "METHOD /users/login HTTP/1.1" STATUS_CODE 41716 "-" "okhttp/3.12.1"
#input = '84.149.236.176 - [2023-05-02 11:50:07.575575] "GET /projects/260 HTTP/1.1" 500 28'

def report(total_size, status_codes):
    print(f"File size: {total_size}")
    for k, v in sorted(status_codes.items()):
        print(f"{k}: {v}")

def parseLogs():
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
                report(total_size, status_codes)
                count = 0
        report(total_size, status_codes)
    except KeyboardInterrupt as e:
        report(total_size, status_codes)
        raise

if __name__ == "__main__":
    parseLogs()