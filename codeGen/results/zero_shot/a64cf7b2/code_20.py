import sys
import heapq

n, m, T = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    edges.append((u, v, t))

pq = []
for u, v, t in edges:
    heapq.heappush(pq, (t, u, v))

dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for u, v, t in edges:
    dp[u][v] = t

for k in range(1, n):
    for i in range(n):
        for j in range(n):
            if dp[i][k] + dp[k][j] < dp[i][j]:
                dp[i][j] = dp[i][k] + dp[k][j]

max_vertices = 0
for i in range(n):
    if dp[0][i] <= T:
        max_vertices = i + 1
        break

print(max_vertices)

visited_vertices = []
curr_time = 0
for i in range(max_vertices):
    for j in range(n):
        if dp[i][j] <= T - curr_time:
            visited_vertices.append(j + 1)
            curr_time += dp[i][j]
            break

print(*visited_vertices, sep=' ')
