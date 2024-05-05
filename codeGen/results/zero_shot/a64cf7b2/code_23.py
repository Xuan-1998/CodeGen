n, m, T = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dp = [0] * (n+1)

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

def dfs(u, time):
    if visited[u]:
        return dp[u]
    visited[u] = True
    dp[u] = 1
    for v, t in graph[u]:
        if time >= t and not visited[v]:
            dp[u] = max(dp[u], dfs(v, time-t) + 1)
    return dp[u]

dp[1] = 0
for i in range(2, n+1):
    dp[i] = dfs(i, T)

k = max(range(n+1), key=lambda x: dp[x])
print(k)
for i in range(2, n+1):
    if dp[i] == k:
        print(i-1, end=' ')
