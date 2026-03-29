import sys

def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = max(0, dp.get(i - c0, [0])[0])

    for j in range(1, m + 1):
        ai, bi, ci, di = map(int, input().split())
        for i in range(n + 1):
            dp[i][j] = max(dp[i - ci][j - 1], dp[i][j - 1]) + di

    return dp[n][m]

print(solve())
