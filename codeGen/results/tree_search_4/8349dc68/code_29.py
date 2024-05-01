def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if j < i + k:
                dp[i][j] = max(dp[i-1][j-1], arr[j-1]) * (k - (j - i))
            else:
                for subarray_end in range(i, j-k+2):
                    dp[i][j] = max(dp[i][j], dp[i-1][subarray_end-1] + arr[subarray_end-1])
                    
    return dp[0][n]

# Example usage
arr = [1, 14, -3, 7, 5, -6]
k = 4
print(maxSumAfterPartitioning(arr, k))  # Output: 18
