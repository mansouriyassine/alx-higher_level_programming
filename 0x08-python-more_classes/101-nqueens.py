#!/usr/bin/python3
"""Solves the N-queens puzzle, finding all possible solutions,
including translations and reflections.

This program uses a virtual backtracking approach without recursion.
It generates solutions for the N-queens puzzle and prints them.

Usage:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.
"""

import sys

if len(sys.argv) != 2:
    print('Usage: ./101-nqueens.py N')
    sys.exit(1)

if not sys.argv[1].isdigit():
    print('N must be a number')
    sys.exit(1)

N = int(sys.argv[1])

if N < 4:
    print('N must be at least 4')
    sys.exit(1)


def initialize_board(board=[]):
    """Initialize a chessboard with the given dimensions."""
    if len(board):
        for row in board:
            row.append(0)
    else:
        for _ in range(N):
            board.append([0])
    return board


def place_queen(board, row, col):
    """Place a queen (represented as 1) on the chessboard."""
    board[row][col] = 1


def is_safe(board, row, col):
    """Check if it's safe to place a queen at the specified position."""
    x = row
    y = col

    for i in range(1, N):
        if (y - i) >= 0:
            # Check up-left diagonal
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            # Check left
            if board[x][y - i]:
                return False
            # Check down-left diagonal
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True


def format_coordinates(candidates):
    """Format the solutions as lists of queen coordinates."""
    solutions = []
    for attempt in candidates:
        solution = []
        for i, row in enumerate(attempt):
            for j, col in enumerate(row):
                if col:
                    solution.append([i, j])
        solutions.append(solution)
    return solutions


candidates = [initialize_board()]

for col in range(N):
    new_candidates = []
    for matrix in candidates:
        for row in range(N):
            if is_safe(matrix, row, col):
                temp = [line[:] for line in matrix]
                place_queen(temp, row, col)
                if col < N - 1:
                    initialize_board(temp)
                new_candidates.append(temp)
    candidates = new_candidates

for item in format_coordinates(candidates):
    print(item)
