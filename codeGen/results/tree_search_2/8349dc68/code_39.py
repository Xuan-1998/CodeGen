def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], arr[i - 1])
        
        for j in range(2, min(i, k) + 1):
            dp[i] = max(dp[i], dp[i - j] + arr[i - j])
            
    return dp[n]
