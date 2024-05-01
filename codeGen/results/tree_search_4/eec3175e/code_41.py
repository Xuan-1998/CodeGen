def has_divisible_subset(n, m, arr):
    dp = [[False] * (m + 1) for _ in range(n)]
    
    for i in range(n):
        for j in range(m + 1):
            if j >= arr[i]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][(j - arr[i]) % m]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return any(dp[n-1][:m+1])
