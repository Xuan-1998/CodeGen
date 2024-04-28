from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

s, t = map(int, input().split())
k, *path = map(int, input().split())

dp = [[False] * (k + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    if i == s:
        continue
    for j in range(k+1):
        if i not in graph[v-1]:
            dp[i][j] = True
        elif path[j-1] != v and dp[path.index(v)][j-1]:
            dp[i][j] = True

print(min(max(dp[i]) for i in range(1, n+1)), max(max(dp[i]) for i in range(1, n+1)))
