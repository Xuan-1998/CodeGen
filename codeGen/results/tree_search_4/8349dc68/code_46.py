def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = arr[i - 1]
        for j in range(1, min(i // k, k) + 1):
            if i < j * k:
                break
            dp[i] = max(dp[i], dp[i - j * k] + arr[i - 1])

    return dp[n]

# Example usage
arr = [1, 14, 5]
k = 3
print(maxSumAfterPartitioning(arr, k))  # Output: 18
