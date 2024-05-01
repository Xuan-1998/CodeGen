n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
k = int(input())
path = list(map(int, input().split()))

dp = [[float('inf'), float('-inf')] for _ in range(n + 1)]
dp[0][0] = dp[0][1] = 0

for i in range(1, k + 1):
    u, v = path[i - 1], path[i]
    if graph[u].index(v) == len(graph[u]) - 1:
        dp[v][0] = min(dp[u][0], 1)
        dp[v][1] = max(dp[u][1], 1)

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if graph[i]:
            dp[j][0] = min(dp[j][0], dp[i][0] + 1)
            dp[j][1] = max(dp[j][1], dp[i][1] + 1)

print(dp[-1])
