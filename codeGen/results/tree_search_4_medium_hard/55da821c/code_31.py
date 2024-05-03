import sys

def solve():
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        s_i, x_i = map(int, input().split())
        for j in range(1, m + 1):
            if j < s_i:
                dp[i][j] = dp[i-1][j]
            elif j == s_i:
                dp[i][j] = min(dp[i-1][s_i] + i, dp[i-1][j])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + 1)

    return sum(max(dp[i]) for i in range(n))
