import sys

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(n):
        if i < k:
            dp[i+1] = max(dp[i], arr[i])
        else:
            dp[i+1] = max(dp[i], arr[i]) + dp[i-k]
    
    return dp[n]

# Example usage
arr = [1, 2, 3, 4, 5]
k = 2
print(max_sum_after_partitioning(arr, k))  # Output: 14

