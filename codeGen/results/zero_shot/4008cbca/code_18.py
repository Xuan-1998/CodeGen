import sys

hand_count = {}
for c in input().strip():
    if c not in hand_count:
        hand_count[c] = 0
    hand_count[c] += 1

min_insertions = float('inf')  

board = input().strip()
insertions = 0

for i in range(len(board)):
    if board[i] in hand_count:
        for _ in range(hand_count[board[i]]):
            while True:
                try_ball = board[i]
                for j in range(1, 4):  
                    if i + j < len(board) and board[i + j] == try_ball:
                        i += j
                        break
                    elif i + j >= len(board):
                        break
                else:  
                    for c in hand_count:
                        if c != try_ball and c in hand_count:
                            board.insert(i, c)
                            insertions += 1
                            break

if len(board) == 0:
    print(insertions)
else:
    print(-1)
