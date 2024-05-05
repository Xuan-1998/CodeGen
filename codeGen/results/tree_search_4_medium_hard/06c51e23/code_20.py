import sys

dp = [[0] * (10**9 + 1) for _ in range(200000 + 1)]

def solve(n, t):
    if n == 0:
        return 0
    
    for i in range(1, n + 1):
        for j in range(1, min(i + 1, t) + 1):
            dp[i][j] = max(dp[i - 1][j], round(int(str(int('9' * (i - 1)) + '.' + str(10 ** i)[1:])), 0))
    
    return dp[n][t]

n, t = map(int, input().split())
print(solve(n, t))
