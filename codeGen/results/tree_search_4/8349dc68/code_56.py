def max_sum_after_partition(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i <= k:
            dp[i] = max(dp[i-1], arr[i-1])
        else:
            dp[i] = max(dp[i-k], arr[i-1])

    return sum(dp[:-1]) - min(arr)
