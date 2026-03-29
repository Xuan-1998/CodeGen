from collections import defaultdict
import sys

n = int(input())
graph = defaultdict(int)
in_degree = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u] += 1
    graph[v] -= 1
    in_degree[v] += 1

capital = max(range(1, n + 1), key=lambda x: in_degree[x])

dp = [0] * (n + 1)
for i in range(2, n + 1):
    for j in range(i):
        if graph[j]:
            dp[i] = max(dp[i], dp[j - 1] + 1)

print(dp[n])
capital_path = [capital]
while capital:
    for city in reversed(range(n)):
        if graph[city]:
            capital = city
            break

    while graph[capital]:
        capital -= 1

    capital_path.append(capital)
    graph[capital] -= 1

for i in range(len(capital_path) - 1, -1, -1):
    print(capital_path[i], end=' ')
