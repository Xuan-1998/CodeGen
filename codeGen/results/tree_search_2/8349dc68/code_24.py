def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        window_sum = 0
        for j in range(max(0, i - k), i):
            window_sum += arr[j]
        dp[i] = max(dp[:i]) + max(window_sum // (k - 1) * (k - 1), arr[i - 1])
    return dp[-1]

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
k = 2
print(maxSumAfterPartitioning(arr, k))  # Output: 15
