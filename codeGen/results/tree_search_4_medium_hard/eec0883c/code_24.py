from collections import deque

n = int(input())
w = [int(input()) for _ in range(n)]
roads = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

dp = [[0] * (w[0]+1) for _ in range(n)]

for i in range(1, n):
    for j in range(w[i-1], -1, -1):
        for u, v, c in roads:
            if i == u and j >= c:
                dp[i][j] = max(dp[i][j], dp[u][j-c] + c)
            elif i == v and j >= c:
                dp[i][j] = max(dp[i][j], dp[v][j-c] + c)

print(max(dp[-1]))
