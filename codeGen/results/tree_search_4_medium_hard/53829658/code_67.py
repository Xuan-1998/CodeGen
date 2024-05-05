import sys
from collections import defaultdict

n = int(input())
in_degree = [0] * (n + 1)
graph = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    in_degree[v] += 1

capital_city = max(range(1, n + 1), key=lambda x: in_degree[x])

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 0
    for j in graph[i]:
        if i != j:
            dp[i][j] = min(dp[i][j], dp[j][i] + 1)

print(max(max(row) for row in dp))
for city in sorted(range(1, n + 1), key=lambda x: in_degree[x], reverse=True):
    print(*[city if i == city else j for i, j in zip(range(1, n + 1), range(n, 0, -1))])
