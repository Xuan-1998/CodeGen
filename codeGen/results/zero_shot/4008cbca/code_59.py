import sys

def can_remove(group):
    return len(set(group)) == 1

def insert_balls(board, hand):
    new_board = list(board)
    while hand:
        ball = hand.pop(0)
        new_board.append(ball)
        for i in range(len(new_board) - 2):
            group = new_board[i:i+3]
            if can_remove(group):
                new_board = new_board[:i] + new_board[i+3:]
                break
    return new_board

def solve(board, hand):
    min_insertions = float('inf')
    for _ in range(len(hand)):
        board = insert_balls(board, hand)
        group_count = 0
        for i in range(len(board) - 2):
            group = board[i:i+3]
            if can_remove(group):
                group_count += 1
        min_insertions = min(min_insertions, len(hand) + len(board) - group_count)
    return -1 if min_insertions == float('inf') else min_insertions

# Read input from stdin
board = sys.stdin.readline().strip()
hand = [sys.stdin.readline().strip() for _ in range(5)]

# Solve the problem and print the answer to stdout
print(solve(board, hand))
