def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i < k:
            dp[i] = max(arr[:i])
        else:
            dp[i] = max(dp[i - 1], arr[i - k:i]) + arr[i]

    return dp[-1]
