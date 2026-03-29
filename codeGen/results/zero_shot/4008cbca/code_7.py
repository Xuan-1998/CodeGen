import sys

board = list(input())
hand = list(input())

result = 0
for i in range(len(board) - 2):
    if board[i] == board[i+1] == board[i+2]:
        j = i + 3
        while j < len(board) and board[j] == board[i]:
            j += 1
        result += (j - i - 2)
        break

if len(hand) == 0:
    result = -1
else:
    for color in set(hand):
        if board.count(color) >= 3:
            result += 1
            board.insert(0, color)
            hand.remove(color)
            break

print(result)
