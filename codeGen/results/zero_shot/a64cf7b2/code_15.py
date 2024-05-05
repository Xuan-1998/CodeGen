from collections import defaultdict

n, m, T = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

# Perform topological sorting on the graph
visited = [False] * (n + 1)
topo_order = []

def dfs(u):
    visited[u] = True
    for neighbor, _ in graph[u]:
        if not visited[neighbor]:
            dfs(neighbor)
    topo_order.append(u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

# Fill up the dp table
dp = [[0] * (T + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(T + 1):
        if i == 1:
            dp[i][j] = 1
        else:
            for prev, t in graph[i]:
                if j >= t and dp[prev][j - t]:
                    dp[i][j] = max(dp[i][j], dp[prev][j - t] + 1)

# Find the maximum and print it
max_vertices = 0
for i in range(1, n + 1):
    if dp[n][T] > max_vertices:
        max_vertices = dp[n][T]

print(max_vertices)
print(' '.join(map(str, [i for i in topo_order if dp[i][T]])))
