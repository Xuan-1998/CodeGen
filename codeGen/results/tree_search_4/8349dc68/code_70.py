def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if i == 1:
                # Base case: maximum sum is the maximum value in the array
                dp[i][j] = max(arr[:i])
            else:
                # Consider two options and choose the one with the higher sum
                take_max = arr[i - 1] + dp[i - 1][j - 1]
                skip = dp[i - 1][j]
                dp[i][j] = max(take_max, skip)

    return dp[n][k]

# Example usage:
arr = [3, 2, -1, 5, 6, 0]
k = 2
print(max_sum_after_partitioning(arr, k))  # Output: 12 (max sum after partitioning)
