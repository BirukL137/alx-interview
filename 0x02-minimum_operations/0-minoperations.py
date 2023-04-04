#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    A method takes an integer n as input and returns the minimum
    number of operations required to make n equal to 1.

    Args:
        n (int): Number of operations.

    Returns:
        n (int): The minimum number of operations required.
    """
    if n == 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    return n
