import sys

board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()

min_insertions = 0
inserted = board

for ball in hand:
    if ball not in inserted:
        min_insertions += 1
        inserted += ball
    else:
        break

print(min_insertions if len(inserted) == len(board) else -1)
