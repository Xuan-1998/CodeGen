import sys
from collections import deque

input()
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp_min = [0] * (n+1)
dp_max = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))

q = deque([(path[0], 0)])
dp_min[path[0]] = dp_max[path[0]] = 0

for i in range(1, k):
    vertex, prev_vertex = q.popleft()
    if path[i] != vertex:
        dp_min[vertex] = min(dp_min[prev_vertex] + (dp_max[prev_vertex] if path[i-1] == prev_vertex else 1), 
                              dp_max[prev_vertex] + (dp_min[prev_vertex] if path[i-1] == prev_vertex else 1))
        dp_max[vertex] = max(dp_min[prev_vertex] + (dp_max[prev_vertex] if path[i-1] == prev_vertex else 1), 
                              dp_max[prev_vertex] + (dp_min[prev_vertex] if path[i-1] == prev_vertex else 1))
    q.append((path[i], vertex))

print(min(dp_min[k]), max(dp_max[k]))
