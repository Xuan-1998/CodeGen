from collections import defaultdict

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for k in range(1, min(i, n // 2) + 1):
        if all(v not in graph[u] for u in range(i - 1)):
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - 1] + (k + 1))
        else:
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - 1])

print(max(dp[n]))
