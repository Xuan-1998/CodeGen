import sys

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    
    # Initialize the dynamic programming table
    dp = [[-float('inf')] * (10**9 + 1) for _ in range(n + 1)]
    
    # Base case: The maximum sum that can be obtained with an empty array is 0.
    dp[0][0] = 0
    
    max_sum = 0
    for i in range(1, n + 1):
        prev_max_val = -1
        for j in range(max(arr[:i], default=0), 10**9 + 1):
            if arr[i-1] <= j:
                dp[i][j] = max(dp[i][j], arr[i-1] + (dp[i-1][max(0, j-arr[i-1])] if i > 1 else 0))
            else:
                dp[i][j] = -float('inf')
            prev_max_val = max(prev_max_val, j)
        max_sum = max(max_sum, dp[i][prev_max_val])
    
    return max_sum

# Read input from stdin
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(max_sum_after_partitioning(arr, k))
