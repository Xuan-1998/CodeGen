n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))
visited = set()

dp = [[0]*T for _ in range(n)]
for i in range(1, n):
    dp[i][0] = 1 if i == 1 else 0

for i in range(1, n):
    for j in range(min(i, T), -1, -1):
        for u, v, t in edges:
            if u == i and v <= n and j >= t:
                dp[v][j] = max(dp[v][j], dp[i][j-t] + 1)

route = [[-1]*T for _ in range(n)]
for i in range(1, n):
    for j in range(min(i, T), -1, -1):
        for u, v, t in edges:
            if u == i and v <= n and j >= t:
                route[v][j] = i if dp[v][j] > dp[route[v][j-1]][j-t] else route[v][j-1]

k = max(dp[n-1])
print(k)
visited = set()
for i in range(1, k+1):
    print(route[n-1][T-k+i], end=' ')
