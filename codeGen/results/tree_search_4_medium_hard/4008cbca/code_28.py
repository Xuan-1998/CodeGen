import sys

board = input()
hand = list(input())

dp = [[0] * 5 for _ in range(len(board) + 1)]

for i in range(1, len(board) + 1):
    for j in range(5):
        if i == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = min(dp[i - 1][k] for k in range(5)) + (1 if board[i - 1] != 'W' and j == hand.index(board[i - 1]) else 0)

if max(dp[-1]):
    print(-1)
else:
    print(max(dp[-1]))
