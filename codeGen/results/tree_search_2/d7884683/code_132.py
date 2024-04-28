def partition_maximum(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    # Base case: single-element array has no partitions
    dp[0] = 0

    for i in range(1, n + 1):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        if left_sum == right_sum:
            # We can partition here, so add the maximum number of partitions for the subarrays
            dp[i] = max(dp[j-1] + 1 for j in range(i+1))
        else:
            # No partition possible at this index, just use the maximum number of partitions from the previous index
            dp[i] = dp[i-1]

    return dp[-1]
