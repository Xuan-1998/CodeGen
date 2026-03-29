import sys

def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for j in range(m + 1):
        if j == 0:
            dp[0][j] = 0
        else:
            a, b, c, d = map(int, input().split())
            dp[c][j] = max(dp[c][j-1], dp[0][j-1]) + d - c
    
    return max(dp[n])

print(solve())
