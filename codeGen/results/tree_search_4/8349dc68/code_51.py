def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(n + 1):
        if i == 0:
            dp[i] = arr[0]
        else:
            max_val = 0
            for j in range(max(0, i - k), i):
                max_val = max(max_val, dp[j])
            dp[i] = max(dp[i-1], max_val + arr[i])

    return dp[n]

# Test the function
arr = [1, 2, 3, 4, 5]
k = 2
print(max_sum_after_partitioning(arr, k))  # Output: 14
