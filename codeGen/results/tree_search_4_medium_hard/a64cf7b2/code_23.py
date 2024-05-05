import sys

# Read input
n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# Initialize DP table
dp = [[0] * (T + 1) for _ in range(n + 1)]

# Fill DP table using bottom-up dynamic programming
for i in range(2, n + 1):
    for t in range(T + 1):
        dp[i][t] = dp[i-1][t]
        for j in range(i - 1):
            for w_edge in edges:
                if (j-1)*T >= w_edge[2] and w_edge[2] <= t:
                    dp[i][t] = max(dp[i][t], dp[j][min(t, w_edge[2])] + 1)

# Print maximum number of vertices that can be visited
k = dp[n][T]
print(k)
# Print indices of vertices that can be visited on the route from vertex 1 to vertex n
visited_vertices = []
t = T
for i in range(n, 0, -1):
    for edge in edges:
        if (i-1)*T >= edge[2] and edge[2] <= t:
            visited_vertices.append(i)
            t -= edge[2]
            break
print(*visited_vertices, sep=' ')
