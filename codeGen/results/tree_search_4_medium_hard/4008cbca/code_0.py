import sys

def solve():
    n, m = map(int, input().split())
    board = list(input())
    hand = list(input())

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        if board[i - 1] == board[i - 2]:
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][0] = dp[i - 1][0] + 1
    for j in range(1, m + 1):
        if hand[j - 1] == hand[j - 2]:
            dp[0][j] = dp[0][j - 1]
        else:
            dp[0][j] = dp[0][j - 1] + 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i - 1] == hand[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[n][m]

print(solve())
