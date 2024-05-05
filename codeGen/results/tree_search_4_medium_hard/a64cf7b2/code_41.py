import sys

n, m, T = map(int, input().split())
dp = [[0] * (T + 1) for _ in range(n + 1)]
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort(reverse=True)

for w, u, v in edges:
    for t in range(w, T + 1):
        dp[u][t] = max(dp[u][t], dp[v][t - w] + 1)

k = 0
max_vertices = 0
for i in range(1, n + 1):
    if dp[i][T]:
        k += 1
        max_vertices = max(max_vertices, i)
print(k)
print(*range(1, max_vertices + 1), sep='\n')
