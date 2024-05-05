import sys
from collections import defaultdict

def solve(n, k, edges):
    # Initialize dp table with False values
    dp = [[False] * (k + 1) for _ in range(n + 1)]

    # Iterate over leaf nodes (nodes with no children)
    for i in range(1, n + 1):
        if not edges[i - 1]:
            dp[i][0] = True

    # Fill up the dp table using dynamic programming
    for j in range(1, k + 1):
        for i in range(j, n + 1):
            children = [edge[1] for edge in edges if edge[0] == i]
            for child in children:
                if dp[child][max(0, j - 1)]:
                    dp[i][j] = True
                    break

    # Print the result based on the last column of the dp table
    print("YES" if dp[n][k] else "NO")

# Read input from stdin
n, k = map(int, sys.stdin.readline().split())
edges = []
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

solve(n, k, edges)
