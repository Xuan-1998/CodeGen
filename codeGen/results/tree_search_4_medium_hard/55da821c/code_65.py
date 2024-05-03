import sys

def min_replant(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        s_i, x_i = map(int, input().split())
        
        for j in range(1, m + 1):
            if s_i == j:
                min_cost = float('inf')
                for k in range(1, j):
                    cost = (x_i - dp[i-1][k]) / (k - j)
                    min_cost = min(min_cost, cost)
                dp[i][j] = dp[i-1][s_i] + int(min_cost) if s_i != 0 else int(min_cost)
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[n][m]

n, m = map(int, input().split())
print(min_replant(n, m))
