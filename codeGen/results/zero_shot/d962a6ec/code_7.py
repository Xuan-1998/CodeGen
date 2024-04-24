import sys

def min_weight_triangulation(n):
    # Initialize dp array with infinity
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    # Base cases
    for i in range(1, n + 1):
        dp[i][i] = 0
        if i < n:
            dp[i][i + 1] = 0
    
    # Fill dp array
    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + i * j * k)
    
    return dp[1][n]

# Read input from stdin
n = int(input().strip())

# Get the minimum weight of triangulation
result = min_weight_triangulation(n)

# Print the result to stdout
print(result)
