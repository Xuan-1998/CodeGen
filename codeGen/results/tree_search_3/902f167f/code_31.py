import sys
from math import sqrt

def min_squares(n, m):
    dp = [[float('inf')] * (m+1) for _ in range(n+1)]
    dp[0] = [0] * (m+1)
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(i):
                if (i-k)**2 <= j:
                    dp[i][j] = min(dp[i][j], dp[k][j-(i-k)**2]+1)
    
    return dp[n][m]

n, m = map(int, sys.stdin.readline().split())
print(min_squares(n, m))
