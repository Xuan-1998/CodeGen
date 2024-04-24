import sys

# Read the number of vertices from standard input
n = int(sys.stdin.readline().strip())

# Initialize the dp table
dp = [[0] * (n+1) for _ in range(n+1)]

# Fill the dp table
for gap in range(2, n):
    for i in range(1, n-gap+1):
        j = i + gap
        dp[i][j] = float('inf')
        for k in range(i+1, j):
            weight = i * k * j
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + weight)

# The answer is the minimum weight triangulation of the full polygon
print(dp[1][n-1])
