import sys

board = input().strip()
hand = input().strip()
removed = False
inserted = 0

def can_remove(board):
    for i in range(len(board) - 2):
        if board[i] == board[i+1] == board[i+2]:
            return True
    return False

while not removed and inserted < len(hand):
    if can_remove(board):
        removed = True
    else:
        for c in hand:
            inserted += 1
            board = f"{board[:-1]}{c}"

print(inserted) if removed else print(-1)
