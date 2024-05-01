from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))

dp = [[(0, 0)] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = (0, 0)

for j in range(1, k + 1):
    dp[path[j-1]][j] = (0, 0)

for j in range(k - 1, -1, -1):
    for i in range(path[j], path[j-1], -1):
        if graph[i]:
            for v in graph[i]:
                if v != path[j-1]:
                    dp[v][j] = min((dp[i][j-1][0] + 1, max(dp[i][j-1][1], dp[v][j-1][0])), (dp[i][j-1][1], max(dp[i][j-1][0], dp[v][j-1][1])))
    if j == k - 1:
        break

print(*[max(0, x) for x in dp[path[k-1]][k]], sep=' ')
