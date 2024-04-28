import sys

def solve():
    m, n = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for j in range(1, m + 1):
        dp[0][j] = 1
    
    for i in range(1, n + 1):
        for k in range(1, min(i, m) + 1):
            dp[i][k] = (dp[i - 1][k - 1] if k > 0 else 0) + sum(dp[i - 1][jj] for jj in range(k))
    
    return pow(dp[n][m], -1, 1000000007)

print(solve())
