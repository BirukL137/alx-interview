#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    A method that takes n x n 2D matrix, returns rotated matrix at
    90 degress clockwise.
    """
    size = len(matrix[0])
    for i in range(size - 1, -1, -1):
        for j in range(0, size):
            matrix[j].append(matrix[i].pop(0))
 