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
    for j in range(len(graph[path[i]])):
        if path[i+1] not in graph[path[i]]:
            min_recompute += 1
            max_recompute = max(max_recompute, (len(graph[path[i]]) - 1) * k + len(graph[path[i]]) - j - 1)
            break

print(min_recompute, max_recompute)
