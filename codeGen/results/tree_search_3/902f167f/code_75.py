import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base cases: single row or column can be tiled with one square
    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(m + 1):
        dp[0][j] = 1

    # Recursive relation: min(dp[i-1][j], dp[i][j-1]) + 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[n][m]

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())

# Compute and print the result
print(min_squares(n, m))
