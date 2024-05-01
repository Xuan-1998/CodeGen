n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
k = int(input())
p = list(map(int, input().split()))
dp = [[float('inf')] * (n+1) for _ in range(k+1)]
dp[0][0] = 0

for i in range(1, k+1):
    for j in range(i):
        if p[j-1] == p[i-1]:
            dp[i][j] = min(dp[i][j-1], 1 + dp[j][k])
        else:
            dp[i][j] = min(dp[i][j-1], 1 + dp[j+1][k])

for i in range(k): print(min(dp[i]), max(dp[i]))
