def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = {0: 0}
    
    for i in range(k, n + 1):
        max_val = max(arr[i-k:i])
        if i - k not in dp:
            dp[i - k] = 0
        dp[i] = max(dp.get(i-1, 0) + max_val, 0)
    
    return dp[n]
