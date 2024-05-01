def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_sum = 0
        for j in range(max(0, i - k), i):
            max_sum = max(max_sum, dp[j] + arr[i - 1])
        dp[i] = max(dp[i - 1], max_sum)

    return dp[n]
