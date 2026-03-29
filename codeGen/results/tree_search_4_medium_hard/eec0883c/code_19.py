from collections import defaultdict

n, w = map(int, input().split())
dp = [[0] * (w + 1) for _ in range(n)]
graph = defaultdict(list)

for _ in range(n - 1):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

def dfs(i, j):
    if i < 0 or i >= n or j < 0:
        return 0
    if dp[i][j] > 0:
        return dp[i][j]
    
    res = 0
    for next_i, next_c in graph[i]:
        res = max(res, dfs(next_i, min(j - next_c, w)))
    dp[i][j] = res + j
    return dp[i][j]

print(dfs(1, w))
