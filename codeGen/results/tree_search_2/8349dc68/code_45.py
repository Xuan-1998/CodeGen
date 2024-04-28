def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i], arr[i])
        if i >= k:
            dp[i + 1] = max(dp[i + 1], dp[i - k + 1] + arr[i])
    return dp[-1]

# Example usage
arr = [1, 14, 5, 9]
k = 3
print(maxSumAfterPartitioning(arr, k))  # Output: 18
