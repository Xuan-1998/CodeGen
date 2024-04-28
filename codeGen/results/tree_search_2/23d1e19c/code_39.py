from collections import deque

def min_max_recomputations(n, m, edges, k, p):
    # Create a graph from the edge list
    graph = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        graph[u].append(v)
        if u != 0 and u < v:  # Avoid adding duplicate edges
            graph[v].append(u)

    # Initialize the dynamic programming table
    dp = [[float('inf'), float('-inf')] for _ in range(n+1)]

    # Base case: no recomputations needed at the start of the path
    dp[p[0]][0] = [0, 0]

    # Iterate over the edges and update the dynamic programming table
    for i in range(1, n+1):
        if i not in p:
            continue
        j = len(p) - 1 - (p.index(i))
        dp[i][j] = [dp[p[j-1]][j-1][0] + 1, dp[p[j-1]][j-1][1] + 1]

    # Find the minimum and maximum number of recomputations
    min_recomputations = min(dp[-1][k-1])
    max_recomputations = max(dp[-1][k-1])

    return [min_recomputations, max_recomputations]
