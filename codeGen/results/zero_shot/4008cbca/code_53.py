import sys

board = input().strip()
hand = input().strip()

n = len(board)
m = len(hand)

min_insertions = 0

if n > m * 3:
    print(-1)
    sys.exit()

current_ball = board[0]

for i in range(1, n):
    if board[i] == current_ball:
        continue
    current_ball = board[i]
    min_insertions += 1

print(min_insertions)
