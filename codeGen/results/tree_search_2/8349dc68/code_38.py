def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], arr[i - 1])
        
        if i >= k:
            dp[i] = max(dp[i], dp[i - k] + arr[i])

    return dp[n]
