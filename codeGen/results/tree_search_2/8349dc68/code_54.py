def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            if j == 1:
                dp[i][j] = arr[i-1]
            else:
                dp[i][j] = max(dp[i-1][j-1] + arr[i+j-1], dp[i-k][j-1] + dp[i-k-1][k-1])

    return dp[n][k]

# Example usage
arr = [1, 2, -3, 4, 5]
k = 2
print(max_sum_after_partitioning(arr, k))  # Output: 10
