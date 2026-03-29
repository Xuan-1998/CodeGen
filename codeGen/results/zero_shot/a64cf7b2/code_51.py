import sys

# Read input
n, m, T = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    edges.append((u, v, t))

# Preprocess the graph
graph = [[] for _ in range(n+1)]
for u, v, t in edges:
    graph[u].append((v, t))

# Perform DFS and dynamic programming
dp = [0] * (n+1)
visited = [False] * (n+1)
def dfs(v, time):
    if visited[v]:
        return 0
    visited[v] = True
    for neighbor, edge_time in graph[v]:
        if time + edge_time <= T:
            dp[neighbor] = max(dp[neighbor], dfs(neighbor, time + edge_time) + 1)
    return dp[v]

# Print the result
k = dfs(1, 0)
print(k)

# Print the indices of vertices that can be visited on the route
visited = [False] * (n+1)
route = []
def backtrack(v):
    if v == n:
        return
    for neighbor, edge_time in graph[v]:
        if time + edge_time <= T and not visited[neighbor]:
            visited[neighbor] = True
            route.append(neighbor)
            backtrack(neighbor)
            visited[neighbor] = False

backtrack(1)
print(*route, sep=' ')
