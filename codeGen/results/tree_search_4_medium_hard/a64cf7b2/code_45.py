import sys
from collections import defaultdict

# Read input
n, m, T = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

dp = [[0] * (T + 1) for _ in range(n + 1)]
memo = {}

def dfs(u, t):
    if (u, t) in memo:
        return memo[(u, t)]
    if dp[u][t] > 0:
        return dp[u][t]
    if t < 0:
        return 0
    max_visit = 0
    for v, tt in graph[u]:
        if tt <= t:
            max_visit = max(max_visit, dfs(v, t - tt) + 1)
    memo[(u, t)] = max_visit
    dp[u][t] = max_visit
    return max_visit

max_visit = dfs(1, T)
print(max_visit)

visited = []
def backtrack(u, t):
    if (u, t) in memo:
        visited.append(u)
        for v, tt in graph[u]:
            if tt <= t and u not in visited:
                backtrack(v, t - tt)
        return
    if dp[u][t] > 0:
        visited.append(u)
        for v, tt in graph[u]:
            if tt <= t and u not in visited:
                backtrack(v, t - tt)
        return

backtrack(n, T)

print(*visited[1:], sep='\n')
