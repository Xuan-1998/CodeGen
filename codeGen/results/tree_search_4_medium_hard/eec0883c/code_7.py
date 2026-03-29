import sys

n, *w = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))

dp = [[0] * (max(w) + 1) for _ in range(n)]

dp[0][w[0]] = w[0]
for i in range(1, n):
    for j in range(max(w) + 1):
        if graph[i]:
            p, c = graph[i][0]
            if dp[p][j-c] + c <= w[i]:
                dp[i][j] = max(dp[i][j], dp[p][j-c] + c)

print(max(dp[-1]))
