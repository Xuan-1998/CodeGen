def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            max_sum = 0
            for last_index in range(j-1, -1, -1):
                max_sum = max(max_sum, dp[i-1][last_index] + max(arr[last_index:i]))
            dp[i][j] = max_sum

    return dp[n][k]
