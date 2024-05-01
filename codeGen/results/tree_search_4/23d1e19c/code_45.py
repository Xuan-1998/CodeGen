===BEGIN SOLUTION===
from collections import deque

def solve(n, m, edges, k, path):
    # Build the graph
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)

    # Initialize dp and dp_max arrays
    dp = [[float('inf')] * (k + 1) for _ in range(n+1)]
    dp_max = [0] * (n+1)

    # Set the base case values
    for i, p_i in enumerate(path):
        if i > 0:
            dp[p_i][i-1] = i - 1
            dp_max[p_i] = k - 1

    # Perform dynamic programming
    for u in range(1, n+1):
        for j in range(k + 1):
            min_recomputation = float('inf')
            for v in graph[u]:
                if p_v != path[-1]:  # Check if the edge is not part of the fixed path
                    min_recomputation = min(min_recomputation, dp[v][j-1] + 1)

            dp[u][j] = min_recomputation

    return str(min(dp[n][k]), max(dp_max))

===END SOLUTION===
