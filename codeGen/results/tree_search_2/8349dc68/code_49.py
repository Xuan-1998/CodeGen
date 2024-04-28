def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(n + 1):
        dp[i] = max(dp[i - 1], arr[i - 1])
        
    for i in range(k, n + 1):
        curr_max = 0
        for j in range(1, min(i, k) + 1):
            curr_max = max(curr_max, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + curr_max * j)
            
    return dp[n]
