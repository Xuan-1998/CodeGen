from sys import stdin

n, m, T = map(int, stdin.readline().split())
dp = [[0] * (T + 1) for _ in range(n + 1)]
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, t = map(int, stdin.readline().split())
    edges[u].append((v, t))

def dfs(u, t):
    if dp[u][t]:
        return dp[u][t]
    
    max_visit = 0
    for v, w in edges[u]:
        if w <= t:
            visit = dfs(v, t - w) + 1
            max_visit = max(max_visit, visit)
    
    dp[u][t] = max_visit if max_visit else 0
    return dp[u][t]

print(dfs(1, T))

for i in range(T, 0, -1):
    if dfs(1, i) > 0:
        print(i, end=' ')
