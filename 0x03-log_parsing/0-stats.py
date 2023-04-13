#!/usr/bin/env python3
"""
A script that reads stdin line by line and computes metrics.
"""

import sys


# Define the list of possible status codes
possible_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {code: 0 for code in possible_status_codes}


def print_statistics():
    """Print the current statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")


try:
    # Loop through stdin line by line
    for i, line in enumerate(sys.stdin, 1):
        # Split the line into components
        components = line.strip().split()

        # Check if the line has the expected number of components
        if len(components) != 7:
            # Skip the line if it doesn't match the expected format
            continue

        # Extract the components
        ip_address = components[0]
        date = components[3][1:]
        status_code = components[5]
        file_size = components[6]

        # Check if the status code is an integer and in the list of
        # possible status codes
        if (not status_code.isdigit() or int(status_code)
                not in possible_status_codes):
            # Skip the line if the status code is not valid
            continue

        # Update metrics
        total_file_size += int(file_size)
        status_code_counts[int(status_code)] += 1

        # Print statistics after every 10 lines
        if i % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Print final statistics on keyboard interruption
    print_statistics()
    raise
