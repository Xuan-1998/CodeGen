import sys

def can_remove_all(board):
    # Your implementation here
    pass

board = input().strip()
hand = input().strip()

to_remove = set()
balls_to_insert = 0

for i in range(len(board)):
    if board[i] in hand:
        to_remove.add(board[i])
        balls_to_insert += 1

if len(to_remove) == len(set(board)):
    print(balls_to_insert)
else:
    print(-1)
