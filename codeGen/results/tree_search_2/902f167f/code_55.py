def min_squares(n, m):
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # base case: when i == 1, only one square is possible
    for j in range(m+1):
        dp[1][j] = 1
    
    for i in range(2, n+1):
        for j in range(2, m+1):
            dp[i][j] = min(dp[i-1][k] + dp[i][j-k] for k in range(1, min(i, j)+1))
    
    return dp[n][m]

# receive input from stdin
n, m = map(int, input().split())
print(min_squares(n, m))
