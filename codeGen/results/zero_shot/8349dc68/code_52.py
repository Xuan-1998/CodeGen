def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = 0
        j = 1
        while j <= min(i, k) and j <= max_val:
            max_val = max(max_val, arr[j - 1])
            dp[i] = max(dp[i], dp[i - j] + max_val * j)
            j += 1
    return dp[n]
