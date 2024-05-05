import sys
from collections import Counter

# Read input
board = input().strip()
hand = list(input().strip())

# Count the colors on the board
board_counts = Counter(board)

# Sort the hand by color count
hand.sort(key=lambda x: (board_counts[x], -hand.count(x)))

# Initialize removed and inserted counts
removed, inserted = 0, 0

for i in range(len(board)):
    if board[i] == hand[0]:
        # If we can remove the current group, do so
        while i < len(board) and board[i] == board[i-1]:
            removed += 1
            i -= 1
        inserted += 1
        hand.pop(0)

# Return the difference between removed and inserted counts
print(inserted - removed)
