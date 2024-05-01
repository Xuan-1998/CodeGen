import sys

def max_points_to_earn():
    n = int(input())
    sequence = list(map(int, input().split()))
    
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for k in range(i+1):
            if k == 0:
                dp[i][k] = i
            else:
                dp[i][k] = max(dp[i-1][max(0, k-1)], min(i, dp[i-1][k]))
    
    return dp[n][n]

print(max_points_to_earn())
