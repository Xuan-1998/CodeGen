n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
s, t = map(int, input().split())
k = int(input())
path = list(map(int, input().split()))
min_recomputations = 0
max_recomputations = 0

