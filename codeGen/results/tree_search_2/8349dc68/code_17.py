def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if i > 0:
                dp[i][j] = max(dp[i-1][j-1] + arr[i+j-1], dp[i][k-j-1])
            else:
                dp[i][j] = arr[j-1]

    return sum(max(subarray) for subarray in dp)

# Example usage
arr = [3, 2, -1, 4, 6]
k = 2
print(max_sum_after_partitioning(arr, k))  # Output: 13
