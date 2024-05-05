import sys

def solve():
    n, m, c0, d0 = map(int, input().split())
    ai = [int(input()) for _ in range(m)]
    bi = [int(input()) for _ in range(m)]
    ci = [int(input()) for _ in range(m)]
    di = [int(input()) for _ in range(m)]

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i >= c0 and j >= bi[j - 1]:
                dp[i][j] = max(dp[i][j], di[j - 1] + dp[i - ci[j - 1]][j - 1])
            elif i >= c0:
                dp[i][j] = max(dp[i][j], d0)
            else:
                dp[i][j] = 0

    return dp[n][m]

print(solve())
