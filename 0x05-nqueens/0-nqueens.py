#!/usr/bin/env python3
"""
0. N queens
"""

import sys


def nqueens(n):
    """
    This function prints every possible solution to the N queens puzzle.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(board, row, col):
        """ Validate the board with row and columns and returns boolean. """
        for r, c in board:
            if r == row or c == col or r - c == row - col\
                  or r + c == row + col:
                return False
        return True

    def backtrack(board, row):
        """
        This function incrementally builds candidate to the solution
        and abandons it, if the validation failed
        """
        if row == n:
            print(board)
            return
        for col in range(n):
            if is_valid(board, row, col):
                board.append([row, col])
                backtrack(board, row + 1)
                board.pop()

    backtrack([], 0)


if __name__ == "__main__":
    """
    If the user called the program with the wrong number of arguments,
    prints Usage: nqueens N, followed by a new line, and exit with the
    status 1
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
