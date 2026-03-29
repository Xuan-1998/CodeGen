codeblock:
import sys

board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()
removed_balls = 0
inserted_balls = 0

for i in range(len(board) - 2):
    if board[i] == board[i+1] == board[i+2]:
        removed_balls += 3
        break

inserted_balls = len(board) - removed_balls

if inserted_balls > 0 and removed_balls >= len(board):
    print(-1)
else:
    print(inserted_balls)

