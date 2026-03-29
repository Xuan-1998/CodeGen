import sys

n, m, T = map(int, input().split())
dp = [[0] * (T + 1) for _ in range(n + 1)]
edges = []

for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

for i in range(1, n + 1):
    dp[i][0] = 1

for u, v, t in edges:
    for j in range(T, t - 1, -1):
        if dp[u][j - t]:
            dp[v][j] = max(dp[v][j], dp[u][j - t] + 1)

k = max([i for i in range(1, n + 1) if dp[i][T]])
print(k)
for i in range(T, -1, -1):
    if k > 0 and dp[k][i]:
        print(k, end=' ')
        break
