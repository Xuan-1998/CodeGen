import sys

def min_weight_triangulation(n):
    # Initialize the dp array with dimensions (n+1) x (n+1)
    dp = [[0 if j == i + 1 else float('inf') for j in range(n+1)] for i in range(n+1)]
    
    # Dynamic programming to find the minimum weight of triangulation
    for gap in range(2, n):
        for i in range(1, n-gap+1):
            j = i + gap
            for k in range(i+1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + i*j*k)
    return dp[1][n]

# Read input from stdin
n = int(sys.stdin.readline().strip())

# Compute and print the answer to stdout
print(min_weight_triangulation(n))
