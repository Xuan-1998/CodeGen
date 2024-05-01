import sys

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
fixed_path = list(map(int, input().split()))
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

dp = [[sys.maxsize] * (len(fixed_path) + 1) for _ in range(n + 1)]

for i in range(len(fixed_path)):
    dp[fixed_path[i]][0] = 0
for v in range(1, n + 1):
    for i in range(len(fixed_path) + 1):
        if i == 0:
            continue
        if fixed_path[i - 1] != v:
            for u in graph[v]:
                dp[u][i] = min(dp[u][i], dp[v][i - 1] + 1)
        else:
            dp[v][i] = dp[fixed_path[i - 1]][i - 1] + 1

min_recomputation, max_recomputation = float('inf'), 0
for i in range(len(fixed_path) + 1):
    min_recomputation = min(min_recomputation, dp[fixed_path[-1]][i])
    max_recomputation = max(max_recomputation, dp[fixed_path[-1]][i])

print(min_recomputation, max_recomputation)
