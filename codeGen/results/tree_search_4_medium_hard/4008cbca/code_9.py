import sys
from collections import deque

board = input().strip()
hand = list(input().strip())
dp = [[0] * (len(hand) + 1) for _ in range(len(board) + 1)]

for i in range(1, len(board) + 1):
    for k in range(1, len(hand) + 1):
        if board[i - 1] == hand[k - 1]:
            dp[i][k] = min(dp[i - 1][k], dp[i][k - 1]) + 1
        else:
            dp[i][k] = dp[i - 1][k] + 1

if dp[-1][-1] == 0:
    print(-1)
else:
    print(dp[-1][-1])
