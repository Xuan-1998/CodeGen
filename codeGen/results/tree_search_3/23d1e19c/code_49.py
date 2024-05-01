from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

s, t, k = map(int, input().split())
path = list(map(int, input().split()))

dp = [[[0, 0] for _ in range(2)] for _ in range(n+1)]

for i in range(n+1):
    if i == s:
        dp[i][0][0] = 0
        dp[i][0][1] = 0
    elif i == t:
        dp[i][0][0] = 0
        dp[i][0][1] = 0
    else:
        for j in range(s, t+1):
            if j not in graph[i]:
                continue
            if j in path:
                dp[i][0][0] = min(dp[j][0][0], dp[j][0][1])
                dp[i][0][1] = max(dp[j][0][0], dp[j][0][1])
            else:
                dp[i][0][0] = min(dp[j][0][0]+(i==j), dp[j][0][1]+(i!=j))
                dp[i][0][1] = max(dp[j][0][0]+(i==j), dp[j][0][1]+(i!=j))

print(f"{dp[t][0][0]} {dp[t][0][1]}")
