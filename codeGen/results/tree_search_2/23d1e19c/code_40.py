import sys
from heapq import heappop, heappush

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))
s, t = path[0], path[-1]

dp_min = [[float('inf')] * (n + 1) for _ in range(n + 1)]
dp_max = [[-1] * (n + 1) for _ in range(n + 1)]

dp_min[s][0] = 0
dp_max[t][0] = 0

pq = [(0, s, 0)]

while pq:
    d, v, rec = heappop(pq)
    if rec > dp_min[v][rec]:
        continue
    for to in graph[v]:
        new_rec = rec + (to != t)
        dp_min[to][new_rec] = min(dp_min[to][new_rec], d + 1)
        dp_max[to][new_rec] = max(dp_max[to][new_rec], d + 1)
        heappush(pq, (d + 1, to, new_rec))

print(min(max(dp_min[t]), max(dp_max[t])))
