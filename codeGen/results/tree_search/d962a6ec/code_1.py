import sys

def min_weight_triangulation(n):
    # Initialize the DP table with zeros
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Base case: No need to fill in as the default values are already 0

    # Fill the DP table
    for length in range(3, n + 1):  # length of the sub-polygon
        for i in range(1, n - length + 2):  # starting vertex of the sub-polygon
            j = i + length - 1  # ending vertex of the sub-polygon
            dp[i][j] = sys.maxsize  # Initialize with infinity
            # Try all possible intermediate vertices k
            for k in range(i + 1, j):
                # Calculate the weight of the triangle and add it to the min weight of two sub-polygons
                cost = i * j * k + dp[i][k] + dp[k][j]
                # Update the DP table with the minimum cost
                dp[i][j] = min(dp[i][j], cost)

    # The final answer is in dp[1][n]
    return dp[1][n]

# Read input from stdin
n = int(input().strip())

# Compute and print the answer to stdout
print(min_weight_triangulation(n))
