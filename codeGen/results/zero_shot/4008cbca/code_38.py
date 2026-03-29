import sys

def solution():
    board = input().strip()
    hand = input().strip()

    stack = []
    runs = []

    i = 0
    while i < len(board):
        j = i + 1
        while j <= len(board) and board[i] == board[j]:
            j += 1
        runs.append(j - i)
        i = j

    hand_counts = {}
    for color in hand:
        if color not in hand_counts:
            hand_counts[color] = 0
        hand_counts[color] += 1

    total_needed = sum(runs)
    for count in hand_counts.values():
        total_needed += count - 2

    print(total_needed)

solution()
