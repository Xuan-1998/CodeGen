def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = max(arr[:i])
            else:
                dp[i][j] = max(dp[i - k][j - 1], dp[i - 1][j - 1] + max(arr[i - k:i]))

    return dp[n][k]
