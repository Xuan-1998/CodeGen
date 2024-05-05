def max_score(arr):
    n, k, z = arr[0], arr[1], arr[2]
    dp = [[-float('inf')] * (k+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dp[i][0] = sum(arr[:i])
    
    for j in range(1, min(k+1, z+1)):
        for i in range(z+1, n-j+1):
            dp[i][j] = max(dp[i-1][j-1] + arr[i], dp[i-1][j] - arr[i])
    
    return dp[n][k]
