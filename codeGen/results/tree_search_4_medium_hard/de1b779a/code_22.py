import sys

def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = d0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i < c0:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[max(0, i - c0)] + d0)
    
    return dp[n][m]

print(solve())
