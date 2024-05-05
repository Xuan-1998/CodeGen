from collections import defaultdict

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

graph = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(i, j):
    if dp[i][j] > 0:
        return dp[i][j]
    
    max_beauty = 0
    for k in range(1, i + 1):
        if all(edge not in graph[k] for edge in graph[k - 1]):
            beauty = (k * j) + dfs(k - 1, j - 1)
            max_beauty = max(max_beauty, beauty)
    
    dp[i][j] = max_beauty
    return max_beauty

print(dfs(n, m))
