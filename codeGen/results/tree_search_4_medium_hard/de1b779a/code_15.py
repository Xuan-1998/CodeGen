import sys

def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i < c0 or j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-c0][j-1] + (d0 - c0) * d0)

    return dp[n][m]

print(solve())
