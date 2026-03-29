import sys
from math import gcd

# Function to compute the minimum number of operations to make all elements 1
def min_operations_to_make_all_one(arr, n):
    # Initialize the DP table with a large number
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Set the diagonal elements to 0
    for i in range(n):
        dp[i][i] = 0
    
    # If any single element is 1, the entire array can be made into 1s
    for i in range(n):
        if arr[i] == 1:
            return 0
    
    # Fill the DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                # Combine subarrays [i, k] and [k+1, j]
                current_gcd = gcd(arr[k], arr[k + 1])
                if current_gcd == 1:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + 1)
    
    # If the result in DP table is still infinity, it's not possible to make all 1s
    return dp[0][n - 1] if dp[0][n - 1] != float('inf') else -1

# Read input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Compute and print the result
result = min_operations_to_make_all_one(arr, n)
print(result)
