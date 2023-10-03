#!/usr/bin/python3
"""Solves the N queens puzzle and prints all possible solutions."""

import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, len(board), -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_nqueens(n):
    """Solves the N queens puzzle using backtracking."""
    def backtrack(board, col):
        if col >= n:
            solutions.append([[r, c] for r, c in enumerate(board)])
            return

        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(board, col + 1)
                board[row][col] = 0

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solutions = []
    backtrack(board, 0)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
