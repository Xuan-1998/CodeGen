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
max_recompute = k - 1

for i in range(k):
    for j in range(i + 1, k):
        if path[j] in graph[path[i]]:
            min_recompute = max(min_recompute, j - i)
            break

print(min_recompute, max_recompute)
