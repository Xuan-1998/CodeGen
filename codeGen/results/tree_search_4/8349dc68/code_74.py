def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i <= k:
            dp[i] = sum(arr[:i])
        else:
            dp[i] = max(dp[i-1], dp[i-k] + max(arr[i-k:i]))
    
    return dp[n]
