def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        local_max_sum = arr[i - 1]
        
        for j in range(max(1, i - k), i):
            local_max_sum = max(local_max_sum, dp[j] + arr[i - 1])
            
        dp[i] = local_max_sum
        
    return sum(dp)
