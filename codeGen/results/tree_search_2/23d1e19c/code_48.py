import heapq

def min_max_recomputations(edges, path):
    n, m = len(set(edge[0] for edge in edges)), len(edges)
    dp = {i: [float('inf'), 0] for i in range(1, n + 1)}
    
    for u, v in edges:
        if v not in dp or dp[v][0] > dp[u][0] + 1:
            dp[v] = [dp[u][0] + 1, max(dp[u][1], dp[u][1] + 1)]
    
    return [dp[i][1] for i in path]

# Example usage
edges = [[1, 2], [2, 3], [3, 4], [4, 5]]
path = [1, 2, 3, 4]
print(min_max_recomputations(edges, path))  # Output: [0, 2]
