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
min_recomputes = float('inf')
max_recomputes = 0
curr_vertex = path[0]
for i in range(1, k):
    next_vertex = path[i]
    curr_recomputes = 0
    while True:
        if next_vertex not in graph:
            break
        for neighbor in graph[next_vertex]:
            if neighbor == curr_vertex:
                break
            curr_recomputes += 1
        if len(graph[next_vertex]) > curr_recomputes:
            curr_recomputes += 1
        curr_vertex = next_vertex
    min_recomputes = min(min_recomputes, curr_recomputes)
    max_recomputes = max(max_recomputes, curr_recomputes)
print(f"{min_recomputes} {max_recomputes}")
