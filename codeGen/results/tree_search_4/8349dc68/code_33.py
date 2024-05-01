import sys

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Initialize the base case
    for i in range(n+1):
        dp[i][i] = arr[i]
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            max_val = max(arr[i:i+k])
            if j-i+1 <= k:
                dp[i][j] = arr[i]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i][i+j-k]+max_val)
    
    return dp[0][n-1]

# Read input from stdin
arr = [int(x) for x in input().split()]
k = int(input())

print(max_sum_after_partitioning(arr, k))
