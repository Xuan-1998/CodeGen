def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Initialize the first row of the DP table
    for j in range(k + 1):
        dp[0][j] = arr[0]

    # Fill up the rest of the DP table
    for i in range(1, n):
        max_val = max(arr[i:i+k+1])
        for j in range(min(i, k), -1, -1):
            dp[i][j] = max(max_val, dp[i-1][j-1])

    # Calculate the final answer
    max_sum = 0
    for i in range(n-k, n):
        max_sum += arr[i]

    return max_sum + sum(dp[n-1])
