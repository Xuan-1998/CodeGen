import sys
import math

def min_weight_triangulation(n):
    def initialize_dp(n):
        dp = [[math.inf] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        return dp

    dp = initialize_dp(n)

    # Base cases: triangles have zero weight
    for i in range(n - 1):
        dp[i][i + 1] = 0

    # Fill dp table
    for size in range(2, n):
        for i in range(n - size):
            j = i + size
            for k in range(i + 1, j):
                weight = i * k * j
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + weight)

    return dp[0][n - 1]

# Read the input
n = int(sys.stdin.readline().strip())

# Calculate and print the answer
print(min_weight_triangulation(n))
