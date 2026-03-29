import sys

def solve(board, hand):
    removed = set()
    inserted = 0
    
    for ball in board:
        if ball in ['R', 'Y', 'B', 'G', 'W']:
            removed.add(ball)
    
    for color in hand:
        for i in range(len(board)):
            while len([ball for ball in [board[i], board[i+1], board[i+2]] if ball == color]) >= 3:
                inserted += 1
                board = board[:i] + [''] * 3 + board[i+3:]
    
    return -1 if any(ball for ball in board) else inserted

# Read input from stdin
board = list(input())
hand = list(input())

print(solve(board, hand))
