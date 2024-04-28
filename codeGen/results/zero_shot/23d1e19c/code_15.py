n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))

min_recompute = 0
max_recompute = 0

for i in range(k-1):
    u = path[i]
    v = path[i+1]
    if v not in graph[u]:
        min_recompute += 1
    else:
        max_recompute += 1

print(min_recompute, max_recompute)
