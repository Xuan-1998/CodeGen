import sys

# Function to calculate the minimum weight of triangulation
def min_weight_triangulation(n):
    # Initialize the DP array with zeros
    dp = [[0] * n for _ in range(n)]
    
    # Fill the DP array
    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = sys.maxsize
            for k in range(i + 1, j):
                # Calculate the weight of the triangle (i, k, j)
                weight = i * k * j
                # Choose the minimum weight partition
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + weight)
    
    # Since the vertices are labeled from 1 to n, we adjust the indices by 1
    return dp[0][n - 1]

# Read the number of vertices from standard input
n = int(input())

# Output the minimum weight of triangulation
print(min_weight_triangulation(n))
