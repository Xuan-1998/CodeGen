import sys

n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

dp = [0] * n

for u, v, t in edges:
    if dp[u] + t <= T:
        dp[v] = max(dp[v], dp[u] + 1)

k = dp[n-1]
print(k)

visited_vertices = []
for i in range(n):
    if dp[i] == k:
        visited_vertices.append(i)
print(*visited_vertices, sep=' ')
