def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        curr_max = arr[i - 1]

        for j in range(1, min(i, k) + 1):
            if j == 1:
                curr_max = max(curr_max, arr[i - j])
            else:
                curr_max = max(curr_max, dp[i - j])

            dp[i] = max(dp[i], dp[i - j] + curr_max * j)

    return dp[n]
