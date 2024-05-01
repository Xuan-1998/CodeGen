n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u] = graph.get(u, []) + [v]

s, t = map(int, input().split())
k = int(input())

dp = [[(0, 0) for _ in range(k+1)] for _ in range(n)]

for i in range(n):
    if i == s:
        dp[i][0] = (0, 0)
    elif i < t:
        dp[i][0] = (0, 0)
    else:
        dp[i][0] = (0, 1)

for j in range(1, k+1):
    for i in range(1, n-1):
        if i == s:
            dp[i][j] = min(dp[i-1][j-1], (1, 1)), max(dp[i-1][j-1], (1, 1))
        elif i < t:
            dp[i][j] = min(min(dp[i-1][j-1], (1, 1)), min(dp[i-1][j], (0, 0))), max(max(dp[i-1][j-1], (1, 1)), max(dp[i-1][j], (0, 0)))
        else:
            dp[i][j] = min(min(dp[i+1][j-1], (1, 1)), min(dp[i+1][j], (0, 0))), max(max(dp[i+1][j-1], (1, 1)), max(dp[i+1][j], (0, 0)))

print(min(dp[-1][-1]), max(dp[-1][-1]))
