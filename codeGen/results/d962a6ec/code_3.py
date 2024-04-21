import sys

# Function to calculate the minimum weight of triangulation
def min_weight_triangulation(n):
    # Initialize the DP table with 0
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the DP table
    for gap in range(2, n):
        for i in range(n-gap):
            j = i + gap
            dp[i][j] = float('inf')
            for k in range(i+1, j):
                # Calculate the weight of triangle (i, k, j)
                weight = i * k * j
                # Choose the minimum weight
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + weight)

    # The answer is in dp[0][n-1] since we want to triangulate the whole polygon
    return dp[0][n-1]

# Read input from stdin
n = int(sys.stdin.readline().strip())

# Compute and print the answer to stdout
print(min_weight_triangulation(n))
