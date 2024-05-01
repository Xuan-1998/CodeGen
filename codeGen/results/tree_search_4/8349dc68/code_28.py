def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        max_val = 0
        for j in range(min(i, k), -1, -1):
            max_val = max(max_val, arr[i - 1])
            dp[i][j] = max(dp[i - 1][k - 1] + max_val - arr[i - j - 1], dp[i - 1][j - 1])

    return dp[n][k]
