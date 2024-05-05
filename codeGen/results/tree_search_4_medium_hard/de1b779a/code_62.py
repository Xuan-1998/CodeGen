import sys

def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for j in range(m + 1):
        if j == 0:
            dp[0][j] = d0
        else:
            ai, bi, ci, di = map(int, input().split())
            for i in range(1, n + 1):
                dp[i][j] = max(dp[i-1][0], (n - ci) * di)
                if j > 0 and i >= bi:
                    dp[i][j] = max(dp[i][j], dp[i-bi][j-1] + di)

    return dp[n][m]

print(solve())
