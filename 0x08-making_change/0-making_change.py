#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    This function returns the fewest number of coind needed to meet total.
    If total is 0 or less, returns 0. If total cannot be met by any number
    coins, returns -1.
    """
    inc = 0
    if total < 1:
        return 0

    coins.sort(reverse=True)

    for coin in coins:
        if total % coin < total:
            inc += total // coin
            total = total % coin

    if total == 0:
        return inc
    return -1
