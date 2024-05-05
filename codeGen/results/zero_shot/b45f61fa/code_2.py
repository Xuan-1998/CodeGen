code
import sys

def matrix_chain_order(p):
    n = len(p)
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    for i in range(n):
        dp[i][i] = 0
    
    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            min_cost = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
                if cost < min_cost:
                    min_cost = cost
            dp[i][j] = min_cost
    
    return dp[0][n-1]

code
