n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

dp = [0] * (n + 1)
for u, v, t in edges:
    dp[v] = max(dp[v], dp[u] + 1) if dp[u] + t <= T else 0

print(max(dp))
visited = []
for i in range(1, n + 1):
    if dp[i] > 0:
        visited.append(i)
print(*visited, sep=' ')
