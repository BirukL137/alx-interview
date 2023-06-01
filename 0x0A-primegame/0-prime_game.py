#!/usr/bin/python3
"""
Prime Game
"""


def isPrime(num):
    """
    This function checks if the number is prime or not and
    returns True if its Prime, otherwise False.
    """
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def isWinner(x, nums):
    """
    This function returns the winner Player.
    """
    winner = 0
    for round in range(x):
        prime = 1
        for n in range(1, nums[round] + 1):
            if isPrime(n):
                prime += 1
        winner += 1 if prime % 2 == 1 else -1
    return None if winner == 0 else "Ben" if winner > 0 else "Maria"
