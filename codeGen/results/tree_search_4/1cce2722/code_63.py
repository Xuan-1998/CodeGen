# BEGIN SOLUTION
def max_points(a):
    n = len(a)
    k = 100 # maximum number of moves allowed
    
    dp = [[0] * (k+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = i
    for j in range(k+1):
        dp[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if a[i-1] == max(dp[:i]):
                dp[i][j+1] = max(dp[i-1][j], dp[i-1][j+1])
            else:
                dp[i][j+1] = dp[i-1][j]
    
    return dp[n][k]

# END SOLUTION
