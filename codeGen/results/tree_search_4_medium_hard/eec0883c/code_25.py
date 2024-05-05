import sys
from collections import defaultdict

def max_gasoline(n, w, edges):
    # Create an adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v, c in edges:
        graph[u].append((v, c))
        graph[v].append((u, 0))  # Add a reverse edge with 0 capacity

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    parent = [-1] * (n + 1)

    def dfs(city):
        if city == n:
            return w[city]
        visited = [False] * (n + 1)
        for v, c in graph[city]:
            if not visited[v]:
                visited[v] = True
                parent_v = w[city] - c
                if parent_v > dp[city][v]:
                    parent_v = dfs(v)
                    dp[city][v] = min(dp[city][city], c + parent_v)
        return dp[city][n]

    return max(0, dfs(0))

# Read input
n = int(input())
w = list(map(int, input().split()))
edges = []
for _ in range(n - 1):
    u, v, c = map(int, input().split())
    edges.append((u, v, c))

print(max_gasoline(n, w, edges))
