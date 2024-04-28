import sys

def max_sum_subarrays(arr, k):
    n = len(arr)
    dp = {i: 0 for i in range(n + 1)}
    
    for i in range(k, n + 1):
        max_sum = -sys.maxsize
        for j in range(i - k, i):
            max_sum = max(max_sum, dp[j] + arr[i - 1])
        dp[i] = max_sum
    
    return dp[n]

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
print(max_sum_subarrays(arr, k))  # Output: 9
