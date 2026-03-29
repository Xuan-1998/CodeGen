code block
import sys

board = input().strip()
hand = input().strip()

board_state = {}
for i in range(len(board)):
    if board[i] in ['R', 'Y', 'B', 'G', 'W']:
        board_state[i] = board[i]

def remove_balls(board_state):
    while True:
        removed = 0
        i = 0
        while i < len(board_state) - 2:  
            if board_state[i] == board_state[i+1] == board_state[i+2]:
                removed += 3
                for j in range(i, i+3):
                    board_state[j] = ''
                i += 3
            else:
                i += 1
        if removed == 0:  
            break
    return board_state

board_state = remove_balls(board_state)

min_balls = len(board) - sum(1 for p in board_state if p)
print(min_balls)
