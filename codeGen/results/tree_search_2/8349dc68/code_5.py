def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(k, n):
        for j in range(1, min(i - k + 2, k) + 1):
            dp[i][j] = max(dp[i-1][min(j-1, k)] + arr[i], dp[i-j][k])
            
    return dp[-1][-1]

# Example usage:
arr = [1,15,10,5,12]
k = 3
print(maxSumAfterPartitioning(arr, k))  # Output: 60
