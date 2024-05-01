import sys

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))

dp = [[0, 0] for _ in range(k+1)]

for i in range(1, k+1):
    if path[i-1] != path[i]:
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + 1
        dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + 1
    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1

print(*dp[k])
