def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = max(dp[i-1][j], arr[i-1])
            else:
                dp[i][j] = max(dp[i-1][j-1] + max(arr[i-k:i]), dp[i-1][j])

    return max(dp[n][:])

# Example usage
arr = [1, 15, -105, 22, 55, None, 8, -5, 4, None]
k = 3

print(maxSumAfterPartitioning(arr, k))
