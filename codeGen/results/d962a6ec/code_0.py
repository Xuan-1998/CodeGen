import sys

# Function to calculate the minimum weight of triangulation
def min_weight_triangulation(n):
    # Initialize the 2D list dp with dimensions n x n with infinity
    dp = [[float('inf')] * n for _ in range(n)]

    # Base cases: No triangle or a single triangle has weight 0
    for i in range(n):
        dp[i][i] = 0
        if i < n-1:
            dp[i][i+1] = 0

    # Fill the DP table in a bottom-up manner
    for gap in range(2, n):  # gap between i and j
        for i in range(n - gap):
            j = i + gap
            for k in range(i+1, j):
                # Weight of the triangle (i, j, k)
                weight = i+1 * j+1 * k+1
                # Choose the minimum weight partition
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + weight)

    # The answer is the minimum weight triangulation of the whole polygon
    return dp[0][n-1]

# Read input from stdin
n = int(sys.stdin.readline().strip())

# Calculate and print the answer to stdout
print(min_weight_triangulation(n))
