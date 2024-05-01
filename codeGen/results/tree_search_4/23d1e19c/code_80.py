import sys

n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))

dp = [[0, 0] for _ in range(n + 1)]

for i in range(1, k):
    dp[path[i]][0] = min(dp[path[i - 1]][0], dp[path[i - 1]][1])
    dp[path[i]][1] = max(dp[path[i - 1]][0], dp[path[i - 1]][1])

for i in range(k + 1, n):
    for j in graph.get(i, []):
        if j < path[k]:
            dp[i][0] = min(dp[j][0], dp[j][1])
            dp[i][1] = max(dp[j][0], dp[j][1])

print(*dp[-1], sep=' ')
