import sys

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Initialize the base case: maximum sum of a subarray with length 1 is the value itself.
    for i in range(n):
        dp[i][1] = arr[i]
    
    # Fill up the dp table using dynamic programming and memoization.
    for i in range(1, n):
        for j in range(2, min(i + 1, k) + 1):
            max_sum = -sys.maxsize
            for last_element_index in range(max(0, i - j + 1), i + 1):
                max_sum = max(max_sum, dp[last_element_index][min(j - 1, k)] + arr[i])
            dp[i][j] = max_sum
    
    # Return the maximum sum of all possible subarrays.
    return max(dp[-1])

# Read inputs from standard input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(maxSumAfterPartitioning(arr, k))
