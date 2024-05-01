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
p = list(map(int, input().split()))

dp = [float('inf')] * (n + 1)
dp[n] = 0

for k in range(k - 1, -1, -1):
    for j in range(p[k], p[k-1], -1):
        if j == s: continue
        dp[j] = min(dp[j], 1 + max(0, dp[k]))

print(min(dp), max(dp))
