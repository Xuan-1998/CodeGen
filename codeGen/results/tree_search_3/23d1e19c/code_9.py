import sys

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)

k = int(input())
path = [int(x) - 1 for x in input().split()]

dp = [[0, 0] for _ in range(n)]
for i in range(k):
    dp[path[i]] = [0, 0]

for i in range(n):
    for j in graph[i]:
        if i < k:
            continue
        dp[j][0] += dp[i][1]
        dp[j][1] += max(dp[i][0], dp[i][1])

print(min(dp[-1]), max(dp[-1]))
