===BEGIN CODE===
from collections import defaultdict
import sys

n, m, T = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

dp = [(0, 0)]  # dp[i][j] represents the maximum number of vertices that can be visited starting from vertex i and ending at vertex j within time limit T - t

for u in range(1, n + 1):
    for v, t in graph[u]:
        max_vertices = 0
        for i in range(u):
            if dp[i][u - 1] <= T - t:
                max_vertices = max(max_vertices, dp[i][u - 1])
        dp.append((v, max_vertices + 1))

k, *route = max(dp[0], key=lambda x: (x[1], x[0]))
print(k)
print(*route, sep='\n')
===END CODE===
