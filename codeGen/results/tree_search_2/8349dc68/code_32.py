def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(k, n + 1):
        # Calculate the maximum sum of subarrays ending at index i
        dp[i] = max(dp[i - 1], arr[i - k:i].max() + dp[i - k])

    return dp[-1]
