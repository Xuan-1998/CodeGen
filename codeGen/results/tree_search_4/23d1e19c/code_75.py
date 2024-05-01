from collections import deque

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

s, t, k = map(int, input().split())
path = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    if i == s:
        dp[i][0], dp[i][1] = 0, 0
    elif i == t:
        continue
    else:
        prev_path = path[path.index(i)-1]
        if graph[prev_path].index(i) == len(graph[prev_path])-1:
            dp[i][0], dp[i][1] = dp[prev_path][0], dp[prev_path][1]
        else:
            dp[i][0], dp[i][1] = min(dp[prev_path][0]+1, dp[prev_path][1]), max(dp[prev_path][0]+1, dp[prev_path][1])

print(min(max(dp[n][k-1])), max(max(dp[n][k-1])))
