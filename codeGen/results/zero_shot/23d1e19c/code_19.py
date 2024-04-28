n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))
min_recomputes = 0
max_recomputes = 0
current_vertex = path[0]
for next_vertex in path[1:]:
    if next_vertex not in graph[current_vertex]:
        min_recomputes += 1
        max_recomputes += 2
    current_vertex = next_vertex

print(min_recomputes, max_recomputes)
