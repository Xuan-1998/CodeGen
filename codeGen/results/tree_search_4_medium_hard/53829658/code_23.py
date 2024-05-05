import sys

def solve():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    dp = [0] * (n + 1)

    # Read the graph and perform DFS/BFS from the capital
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # This is a directed tree, so we add both edges

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
            dp[node] = min(dp[node], 1 + dp[neighbor])

    # Perform DFS/BFS from the capital (arbitrarily chosen as node 1)
    dfs(1)

    # Find the minimum number of reversed edges needed to reach any other city
    max_dist = max(dp[1:])
    return str(max_dist) + "\n" + " ".join(map(str, [i for i in range(2, n + 1)]))

print(solve())
