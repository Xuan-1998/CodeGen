import sys

def solve():
    n, m = map(int, input().split())
    s = [0] * (n+1)
    x = [0.0] * (n+1)

    dp = [[float('inf')] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        s[i], x[i] = map(int, input().split())
        for j in range(1, m+1):
            if s[i] == j:
                dp[i][j] = min(dp[k-1][k] + (i-k) for k in range(1, j+1))
    return dp[n][m]

print(solve())
