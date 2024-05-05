from collections import defaultdict
import sys

n, m, T = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

dp = [[0] * (T + 1) for _ in range(n + 1)]

def dfs(i, j):
    if dp[i][j] > 0:
        return dp[i][j]
    if j < 0 or i == n:
        return 0

    max_visit = 0
    for v, t in graph[i]:
        remaining_time = j - t
        if remaining_time >= 0 and dfs(v, remaining_time) + 1 > max_visit:
            max_visit = dfs(v, remaining_time) + 1

    dp[i][j] = max_visit
    return max_visit

print(dfs(1, T))
