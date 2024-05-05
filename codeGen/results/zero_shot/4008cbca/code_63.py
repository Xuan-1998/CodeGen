import sys
from collections import deque

def can_remove_all(board):
    queue = deque([(board, 0)])
    while queue:
        board, insertions = queue.popleft()
        if not any(b == b1 and b1 in ['R', 'Y', 'B', 'G'] for b, b1 in zip(board, board[1:])):
            return True
        if not all(len(list(group)) < 3 for key, group in groupby(board)):
            continue
        queue.extend((board[:i] + [b] + board[i:], insertions + 1) for i, (b,) in enumerate(zip(board, board[1:])) if b == b1 and b1 in ['R', 'Y', 'B', 'G'])
    return False

def min_insertions():
    board = input().strip()
    hand = list(input().strip())
    result = 0
    for i, b in enumerate(board):
        if b in ['R', 'Y', 'B', 'G']:
            while hand and [b] * (3 - len(hand)) + hand:
                hand.pop(0)
            if not hand:
                return -1
            else:
                result += 1
    return result

print(min_insertions())
