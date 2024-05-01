def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            max_val = 0
            for subarray_end in range(j - 1, i):
                max_val = max(max_val, arr[subarray_end])
                dp[i][j] = max(dp[i-1][j], dp[i-j][k] + max_val * j)

    return dp[n][k]
