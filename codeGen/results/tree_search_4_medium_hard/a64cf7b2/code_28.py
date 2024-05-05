import sys

n, m, T = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Build dp table
dp = [[0] * (T + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][0] = 1

# Iterate over edges and update dp table
for u, v, t in edges:
    for ti in range(T, t - 1, -1):
        if dp[u][ti] > 0:
            dp[v][ti + t] = max(dp[v][ti + t], dp[u][ti])

# Find the maximum number of vertices that can be visited starting from vertex 1
k = 0
for i in range(T, -1, -1):
    if dp[1][i]:
        k = i
        break

print(k)
if k:
    print(*range(1, n + 1), sep='\n')
else:
    print()
