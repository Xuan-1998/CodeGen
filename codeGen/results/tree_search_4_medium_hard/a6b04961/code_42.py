from collections import defaultdict
import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for t in range(1, n + 1):
    for s in range(min(t - 1, m), -1, -1):
        if dp[t - 1][s] > 0:
            for u in range(1, n + 1):
                if (u not in graph.get(t - 1, []) and
                    dp[u - 1][s - 1] > 0):
                    dp[t][s] = max(dp[t][s], dp[u - 1][s - 1])
        if dp[t][s - 1] > 0:
            for u in range(1, n + 1):
                if (u not in graph.get(t - 1, []) and
                    s < m and dp[u - 1][s - 1] > 0):
                    dp[t][s] = max(dp[t][s], dp[u - 1][s - 1])

print(max(0, max(max(row) for row in dp)))
