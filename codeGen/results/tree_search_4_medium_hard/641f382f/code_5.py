import sys
from math import gcd

def min_operations_to_make_ones(n, arr):
    # If any element is already 1, no operations are needed
    if 1 in arr:
        return 0
    
    # Initialize dp array with a large number
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case for an empty subarray
    
    # Compute the minimum operations for subarrays
    for i in range(1, n + 1):
        current_gcd = 0
        for j in range(i, 0, -1):
            current_gcd = gcd(current_gcd, arr[j - 1])
            if current_gcd == 1:  # If GCD is 1, update dp[i]
                dp[i] = min(dp[i], dp[j - 1] + 1)
    
    # If it's impossible to make all elements 1, return -1
    return dp[n] if dp[n] != float('inf') else -1

# Read input from stdin
n = int(input())
arr = list(map(int, input().split()))

# Print the result to stdout
print(min_operations_to_make_ones(n, arr))
