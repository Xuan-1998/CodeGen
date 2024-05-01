def maxSumAfterPartition(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    max_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        curr_max = arr[i - 1]
        for j in range(min(i, k), -1, -1):
            curr_max = max(curr_max, arr[i - j - 1])
            dp[i][j] = max(dp[i - 1][j], dp[i - j][k] + curr_max)
        max_sum[i] = max(max_sum[i - 1], dp[i][k])

    return max_sum[n]
