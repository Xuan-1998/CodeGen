def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(n + 1):
        if i == 0:
            dp[i] = arr[0]
        else:
            max_val = max(arr[i-k+1:i+1])
            dp[i] = max(max_val + dp[i-k], dp[i-1])

    return dp[n-1]

# Example usage
arr = [3, 2, -1, 4, 6, 5]
k = 2
print(max_sum_after_partitioning(arr, k))  # Output: 18
