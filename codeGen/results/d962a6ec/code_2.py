import sys

def min_weight_triangulation(n):
    # Initialize the dp array with infinity for all values except the base cases
    dp = [[float('inf') if j - i > 1 else 0 for j in range(n)] for i in range(n)]
    
    # Iterate over the length of the chain
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            # Find the minimum weight triangulation for the chain from i to j
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + i * k * j)
    
    # The answer is the minimum weight triangulation for the entire polygon
    return dp[0][n - 1]

# Read input from stdin
n = int(sys.stdin.readline().strip())

# Output the answer to stdout
print(min_weight_triangulation(n))
