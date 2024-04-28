def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    # Initialize the base case when i < k
    for i in range(k):
        dp[i] = max(0, sum(arr[:i+1]))

    # Fill up the DP table from back to front
    for i in range(k, n + 1):
        if i < k:
            dp[i] = max(dp[i-1], dp[i-k] + arr[i-1])
        else:
            dp[i] = dp[i-1] + arr[i-1]

    return max(dp)
