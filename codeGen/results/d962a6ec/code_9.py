import sys

def min_weight_triangulation(n):
    # Initialize the dp array with infinity
    def initialize_dp(n):
        dp = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0  # No triangle can be formed with a single vertex
        return dp
    
    dp = initialize_dp(n)

    # Fill the dp array with the minimum weights
    for gap in range(2, n):  # The difference between i and j
        for i in range(n - gap):
            j = i + gap
            for k in range(i + 1, j):
                # The weight of the triangle i-k-j
                weight = (i + 1) * (k + 1) * (j + 1)
                # The minimum weight of the triangulation
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + weight)
    
    # The minimum weight of triangulating the whole polygon
    return dp[0][n - 1]

# Read input from stdin
n = int(sys.stdin.readline().strip())

# Compute and print the answer to stdout
print(min_weight_triangulation(n))
