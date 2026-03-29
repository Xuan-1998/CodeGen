import sys

n, m, T = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    edges.append((u, v, t))

dp = [0] * (n + 1)
for u, v, t in edges:
    if T - t >= 0:
        dp[v] = max(dp[v], dp[u] + 1)

max_vertices = max(dp[1:i+1] for i in range(2, n+1))

print(max_vertices)
for i in range(n):
    if dp[i+1] == max_vertices:
        print(i+1, end=' ')
