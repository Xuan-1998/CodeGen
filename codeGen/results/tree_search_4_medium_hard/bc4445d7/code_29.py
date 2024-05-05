import sys

# Constants
MOD = 10**9 + 7
MAXN = 10**5

# Function to calculate the maximum sum of f(u,v) values
def solve(n, edges, k):
    dp = [[[0] * (k+1) for _ in range(n)] for _ in range(MAXN)]

    # Initialize the table
    for i in range(1, n):
        for j in range(2, n+1):
            dp[i][j][0] = 0

    # Fill up the table by considering each edge in order from bottom (leaves) to top (root)
    for u, v in edges:
        for k in range(1, k+1):
            # Calculate the value of f(u,v) for all possible ways to label this edge
            for x in range(k+1):
                dp[u][v][k] = max(dp[u][v][k], dp[u-1][v-1][x-1] + (u*v) % MOD)

    # Return the answer, which represents the maximum sum of f(u,v) values over all pairs (u,v)
    return dp[1][0][k] % MOD

# Read input from standard input
n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]
m = int(input())
prime_factors = list(map(int, input().split()))

# Calculate and print the maximum possible distribution index of the tree
print(solve(n, edges, m))
