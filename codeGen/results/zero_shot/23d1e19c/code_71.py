from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))
min_recompute = float('inf')
max_recompute = 0

curr_vertex = path[0]
queue = deque([(curr_vertex, 0)])

while queue:
    vertex, depth = queue.popleft()
    for neighbor in graph[vertex]:
        if neighbor == path[k-1]:
            max_recompute = min(max_recompute, depth)
        elif neighbor not in set(path):
            queue.append((neighbor, depth+1))

print(min_recompute, max_recompute)
