from collections import deque

n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

dp = [[0] * (T + 1) for _ in range(n + 1)]
path = [[] for _ in range(n + 1)]

for i in range(1, n):
    dp[i][T] = 0
for j in range(T + 1):
    dp[0][j] = 0

for u, v, t in edges:
    for j in range(min(t, T), -1, -1):
        if dp[u][j-t] > 0 and dp[v][j] < dp[u][j-t]:
            dp[v][j] = dp[u][j-t]
            path[v].extend(path[u][:])
            path[v].append(u)
    for j in range(T + 1):
        if dp[u][j-t] > 0:
            dp[u][j] = max(dp[u][j], dp[u][j-t] + 1)

k = dp[n-1][T]
print(k)
for i in range(k - 1, -1, -1):
    print(path[n-1][i])
