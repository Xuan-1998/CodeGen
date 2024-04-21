import sys

def min_weight_triangulation(n):
    # Initialize the 2D dp array with zeroes
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the dp array
    for gap in range(2, n):  # gap between i and j
        for i in range(1, n - gap + 1):
            j = i + gap
            dp[i][j] = float('inf')  # Initialize with infinity
            for k in range(i + 1, j):
                weight = i * j * k + dp[i][k] + dp[k][j]
                dp[i][j] = min(dp[i][j], weight)

    # The answer is the minimum weight of triangulating the entire polygon
    return dp[1][n-1]

# Read input from stdin
n = int(sys.stdin.readline().strip())

# Calculate and print the answer
print(min_weight_triangulation(n))
