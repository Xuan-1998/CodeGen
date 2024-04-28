import sys
from heapq import heapify, heappop

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

s, t, k = map(int, input().split())
path = list(map(int, input().split()))
prev_to_t = {v: float('inf') for v in range(1, n + 1)}
for i in range(k - 1):
    prev_to_t[path[i]] = path[i + 1]

dp = [[0, 0] for _ in range(n + 1)]
heapify([(0, s)])

while heap:
    dist, curr = heappop()
    if curr == t:
        break
    for neighbor in graph[curr]:
        new_dist = dist + 1
        prev_to_t[neighbor] = min(prev_to_t[neighbor], curr)
        dp[neighbor][min(dp[neighbor]) - 1] += 1
        dp[neighbor][max(dp[neighbor]) - 1] += 1
        heappush((new_dist, neighbor))
