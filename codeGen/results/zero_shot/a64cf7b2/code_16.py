import sys

n, m, T = map(int, input().split())
graph = {}
for _ in range(m):
    u, v, t = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, t))

dp = {i: 0 for i in range(1, n+1)}
vis = set()

def dfs(vertex):
    if vertex not in vis:
        vis.add(vertex)
        for neighbor, edge_weight in graph.get(vertex, []):
            if edge_weight <= T - dp[neighbor]:
                dp[vertex] = max(dp[vertex], dp[neighbor] + 1)
            dfs(neighbor)

dfs(1)

k = max(dp.values())

print(k)
visited_vertices = [i for i in range(1, n+1) if dp[i] == k]
print(*visited_vertices, sep='\n')
