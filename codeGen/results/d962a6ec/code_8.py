import sys

def min_weight_triangulation(n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for l in range(2, n):
        for i in range(1, n-l+1):
            j = i + l
            dp[i][j] = float('inf')
            for k in range(i+1, j):
                weight = i * j * k
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + weight)
    return dp[1][n-1]

# Read input from stdin
n = int(sys.stdin.readline().strip())
# Calculate and print the answer to stdout
print(min_weight_triangulation(n))
