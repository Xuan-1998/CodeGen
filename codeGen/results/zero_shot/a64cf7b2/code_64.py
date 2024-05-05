import sys

n, m, T = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    edges.append((u, v, t))

graph = {}
for u, v, t in edges:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, t))

in_degree = {u: 0 for u in range(1, n+1)}
for u, v, t in edges:
    in_degree[v] += 1

queue = [u for u in range(1, n+1) if in_degree[u] == 0]
top_order = []
while queue:
    u = queue.pop(0)
    top_order.append(u)
    for v, t in graph.get(u, []):
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

dp = [0] * (n+1)
for i in range(1, n+1):
    for v, t in graph.get(i, []):
        if t <= T and dp[v] + 1 > dp[i]:
            dp[i] = dp[v] + 1

route = []
i = n
while i != 0:
    for v, t in graph.get(i, []):
        if dp[v] + 1 == dp[i]:
            route.append(i)
            i = v
            break
route.reverse()

print(len(route))
print(' '.join(map(str, route)))
