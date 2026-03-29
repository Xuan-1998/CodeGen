import sys
from math import gcd

def solve(n, arr):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return n - arr.count(1)

    # Pre-compute the gcd of all subarrays
    g = [[0]*n for _ in range(n)]
    for i in range(n):
        g[i][i] = arr[i]
        for j in range(i+1, n):
            g[i][j] = gcd(g[i][j-1], arr[j])

    # Initialize a 2D dp table with size n x n, and fill it with a large value
    dp = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if g[i][j] == 1:
                dp[i][j] = j - i

    # Compute dp[i][j] as the minimum of its old value and dp[i][k] + dp[k+1][j] + 1
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + 1)

    # Return the result
    if dp[0][n-1] == float('inf'):
        return -1
    else:
        return dp[0][n-1]

# Read the input
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# Print the output
print(solve(n, arr))

