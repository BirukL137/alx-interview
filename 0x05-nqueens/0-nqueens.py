#!/usr/bin/python3
"""
A program that solves the N queens problem which is the challenge of
placing N non-attacking queens on an N×N chessboard.
"""
import sys


def display_board(board):
    """
    Displays the board with n x n.
    """
    dis = []
    for i, row in enumerate(board):
        val = []
        for j, col in enumerate(row):
            if col == 1:
                val.append(i)
                val.append(j)
        dis.append(val)
    print(dis)


def is_valid(board, row, column, n):
    """
    checks the columns if they are safe both side and diagonally,
    """
    for i in range(row, -1, -1):
        if board[i][column] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(column, n)):
        if board[i][j] == 1:
            return False
    return True


def nqueens(board, row, n):
    """
    This function incrementally builds candidate to the solution
    and abandons it, if the validation failed
    """
    if (row == n):
        display_board(board)
        return True
    res = False

    for i in range(n):
        if (is_valid(board, row, i, n)):
            board[row][i] = 1
            if nqueens(board, row+1, n):
                res = True
            board[row][i] = 0  # BACKTRACK
    return res


def nqn(n):
    """
    creates a new board and finds all posibilities to solve the puzzle.
    """
    board = [[0 for i in range(n)]for i in range(n)]
    if not nqueens(board, 0, n):
        return False
    return True


if __name__ == "__main__":
    """
    If the user called the program with the wrong number of arguments,
    prints Usage: nqueens N, followed by a new line, and exit with the
    status 1
    """
    if (len(sys.argv) == 2):
        try:
            number = int(sys.argv[1])
            nqn(number)
        except Exception:
            print("N must be a number")
            exit(1)
        if number < 4:
            print("N must be at least 4")
            exit(1)
    else:
        print("Usage: nqueens N")
        exit(1)
