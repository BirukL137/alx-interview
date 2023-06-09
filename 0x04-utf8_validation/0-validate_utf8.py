#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    A function that determines if a given data set represents a valid
    UTF-8 encoding.

    Args:
        data (list): represented by a list of integers.

    Returns:
        True, if data is a valid UTF-8 encoding, otherwise False.
    """
    numBytes = 0
    for byte in data:
        if numBytes == 0:
            if (byte >> 5) == 0b110:
                numBytes = 1
            elif (byte >> 4) == 0b1110:
                numBytes = 2
            elif (byte >> 3) == 0b11110:
                numBytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            numBytes -= 1
    return numBytes == 0
