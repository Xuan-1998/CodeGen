import sys

def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        ai, bi, ci, di = map(int, input().split())
        for j in range(n+1):
            if j < c0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j])
            else:
                dp[i][j] = max(dp[i-1][j-ci] + di, dp[i-1][j])
    
    return dp[m][n]

print(solve())
