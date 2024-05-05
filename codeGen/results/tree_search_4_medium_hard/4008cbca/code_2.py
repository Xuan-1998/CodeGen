import sys

board = input().strip()
hand = list(input().strip())

dp = [[0] * (len(hand) + 1) for _ in range(len(board) + 1)]

for i in range(1, len(board) + 1):
    for j in range(len(hand) + 1):
        if board[i - 1] == hand[j - 1]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

result = dp[-1][-1]
print(result if result < len(board) else -1)
