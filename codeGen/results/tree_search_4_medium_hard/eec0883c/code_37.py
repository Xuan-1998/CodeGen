import sys

def solve():
    n, *gas = map(int, input().split())
    dp = [[0] * (10**9 + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        u, v, c = map(int, input().split())
        for j in range(gas[i - 1], -1, -1):
            dp[i][j] = max(dp[i][j], dp[v][min(j - c, gas[i - 1])])
    
    return max(dp[n])

print(solve())
