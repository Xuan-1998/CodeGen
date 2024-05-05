import sys

# Read input from stdin
n = int(input())
w = [0] + list(map(int, input().split()))
graph = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    graph.append((u, v, c))

dp = [[0] * (10**9+1) for _ in range(n+1)]

# Compute dp table
for i in range(2, n+1):
    for j in range(w[i]):
        if j >= w[i-1]:
            for road in graph[i-1:]:
                u, v, c = road
                if j - c >= 0 and dp[road[1]][min(j-c, w[v])]:
                    dp[i][j] = max(dp[i][j], dp[u][min(j-c, w[u])] + j)
        else:
            dp[i][j] = dp[i-1][j]

# Print the maximum amount of gasoline Nut can have at the end of the path
print(max(dp[n]))
