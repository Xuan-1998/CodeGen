def max_sum_after_partition(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n - k + 1)]

    # Base case: maximum sum for subarrays of length 0 is the value at that index
    for i in range(n - k + 1):
        dp[i][0] = arr[i]

    # Calculate maximum sum for each subarray of length k
    for j in range(1, k + 1):
        for i in range(j - 1, n - k):
            dp[i][j] = max(dp[i - 1][j - 1] + arr[i], dp[i - 1][j] + arr[i])

    # Return the maximum sum for the entire array
    return max(dp[0][k], dp[1][k], ..., dp[n - k][k])
