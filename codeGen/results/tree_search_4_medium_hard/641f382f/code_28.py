import sys
from math import gcd

# Function to initialize the dp array with INT_MAX and gcd values
def initialize_dp(n, arr):
    dp = [[[float('inf'), None] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                if arr[i] == 1:
                    dp[i][j][0] = 0
                dp[i][j][1] = arr[i]
            else:
                dp[i][j][1] = gcd(dp[i][j-1][1], arr[j])
    return dp

# Function to compute the minimum operations using dynamic programming
def min_operations(n, arr):
    dp = initialize_dp(n, arr)
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            for k in range(i, j):
                if gcd(dp[i][k][1], dp[k+1][j][1]) == 1:
                    dp[i][j][0] = min(dp[i][j][0], dp[i][k][0] + dp[k+1][j][0] + 1)

    return dp[0][n-1][0] if dp[0][n-1][0] != float('inf') else -1

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result to stdout
print(min_operations(n, arr))
