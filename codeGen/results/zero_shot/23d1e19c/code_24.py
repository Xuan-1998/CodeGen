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

min_rec = float('inf')
max_rec = 0

for i in range(1, k):
    if path[i-1] not in graph or path[i] not in graph:
        break
    min_rec = min(min_rec, len(graph[path[i-1]]) - 1)
    max_rec = max(max_rec, len(graph[path[i-1]]))

print(min_rec, max_rec)
