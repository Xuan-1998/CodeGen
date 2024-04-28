import sys

# Input processing
n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
k = int(input())
path = list(map(int, input().split()))

# Dynamic programming
dp = [[0, 0] for _ in range(n + 1)]
for i in range(2, n + 1):
    if path[i - 1] == i:
        dp[i][0] = min(dp[path[i - 2]][0], 1) if i > 1 else 0
        dp[i][1] = max(dp[path[i - 2]][1], 1) if i > 1 else 0
    for j in range(i):
        if path[j] == i:
            continue
        if path[j + 1] == i:
            break
        dp[i][0] = min(dp[j][0] + 1, dp[i][0])
        dp[i][1] = max(dp[j][1] + 1, dp[i][1])

# Output
print(f"{dp[-1][0]} {dp[-1][1]}")
