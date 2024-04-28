def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(k, n + 1):
        # Calculate the maximum value of the current subarray
        max_val = max(arr[i - k:i])
        # Update the overall maximum sum by adding the maximum value to the previous maximum sum
        dp[i] = max(dp[i - 1], max_val)

    return dp[-1]
