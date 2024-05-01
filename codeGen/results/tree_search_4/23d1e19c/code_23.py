from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
s, t, k = map(int, input().split())
path = list(map(int, input().split()))
dp = [[float('inf'), float('-inf')] for _ in range(n+1)]
dp[s] = [0, 0]

for i in range(1, n+1):
    if i == path[0]:
        dp[i][0] = dp[path[0]][0] + 1
        dp[i][1] = max(dp[i][1], dp[path[0]][1] + 1)
    else:
        for j in range(i-1, -1, -1):
            if graph[j]:
                if j == path[path.index(i)]-1 and i != t:
                    dp[i][0] = min(dp[i][0], dp[j][0]+1)
                    dp[i][1] = max(dp[i][1], dp[j][1]+1)
                elif i != t:
                    dp[i][0] = min(dp[i][0], dp[j][0]+1)
                    dp[i][1] = max(dp[i][1], dp[j][1]+1)

print(min(dp[k]), max(dp[k]))
