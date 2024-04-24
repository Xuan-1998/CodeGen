import sys

def min_weight_triangulation(n):
    # Initialize the dynamic programming table with infinity
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    # Base case: triangles have zero weight
    for i in range(1, n + 1):
        dp[i][i] = 0

    # Fill the table
    for length in range(2, n + 1):  # length of the chain
        for i in range(1, n - length + 2):  # starting vertex
            j = i + length - 1  # ending vertex
            for k in range(i + 1, j):  # intermediate vertex
                # Choose the best k to partition the chain
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + i * j * k)

    # The answer is the minimum weight triangulation from 1 to n
    return dp[1][n]

# Read the input
n = int(sys.stdin.readline().strip())

# Compute and print the answer
print(min_weight_triangulation(n))
