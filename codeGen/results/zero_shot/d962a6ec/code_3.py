import sys

def min_triangulation_weight(n):
    # Initialize the dynamic programming table
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Base cases: single triangles have no internal triangulation
    for i in range(1, n-1):
        dp[i][i+2] = i * (i+1) * (i+2)

    # Fill the DP table
    for length in range(4, n+1):  # Start from quadrilaterals and go up to the full polygon
        for i in range(1, n-length+2):  # Start vertex
            j = i + length - 1  # End vertex
            dp[i][j] = float('inf')  # Initialize with infinity
            for k in range(i+1, j):  # Possible middle vertices
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + i*k*j)

    # The answer is the minimum weight of triangulating the whole polygon
    return dp[1][n]

# Read input
n = int(sys.stdin.readline().strip())

# Calculate and print the answer
print(min_triangulation_weight(n))
