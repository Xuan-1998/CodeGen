def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        current_max = 0
        for j in range(1, min(i, k) + 1):
            current_max = max(current_max, arr[i - j])
            if j >= k:
                dp[i] = max(dp[i], current_max * (i // k) + dp[i - k])
            else:
                dp[i] = max(dp[i], current_max)

    return dp[n]
