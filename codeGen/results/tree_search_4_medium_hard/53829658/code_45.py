from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [float('inf')] * n
dp[0] = 0

visited = [False] * n

def dfs(city):
    if visited[city]:
        return dp[city]
    visited[city] = True
    for neighbor in graph[city]:
        dp[neighbor] = min(dp[neighbor], 1 + dp[city])
    return dp[city]

capital = 0
min_reversals = float('inf')
for i in range(1, n):
    if dfs(i) < min_reversals:
        capital = i
        min_reversals = dfs(i)

print(min_reversals)
result = [0]
dfs(capital)
print(*result[1:], sep='\n')
