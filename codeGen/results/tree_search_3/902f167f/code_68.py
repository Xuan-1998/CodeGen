import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j-1] + (1 if i <= j else 0), 
                               dp[i-1][j] + (1 if i < j else 0))
            elif i == 0 or j == 0:
                dp[i][j] = 1

    return dp[n][m]

n, m = map(int, sys.stdin.read().split())
print(min_squares(n, m))
