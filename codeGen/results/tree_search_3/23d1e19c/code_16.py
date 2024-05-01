import sys
from collections import deque

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))
path += [n]

dp = [[0] * (len(path) + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][0] = float('inf')
dp[0][0] = 0
for j in range(len(path)):
    if path[j] != t:
        dp[path[j]][j + 1] = 1 + max(dp[v][j] for v in graph[path[j]])
    else:
        dp[t][j + 1] = 0

print(min(dp[n][-1]), max(dp[n][-1]))
