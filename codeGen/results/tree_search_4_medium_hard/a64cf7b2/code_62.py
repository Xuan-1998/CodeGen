import sys
from collections import defaultdict

n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

dp = [[0] * (T + 1) for _ in range(n + 1)]

memo = {}
def dfs(i, t):
    if (i, t) not in memo:
        if i == n:
            memo[(i, t)] = 1
        else:
            max_vertices = 0
            for edge in edges:
                u, v, time_taken = edge
                if u == i and time_taken <= t:
                    neighbor = next(j for j in range(1, n+1) if (j, v) not in edges)
                    vertices_visitted = dfs(neighbor, t - time_taken) + 1
                    max_vertices = max(max_vertices, vertices_visitted)
            memo[(i, t)] = max_vertices
    return memo[(i, t)]

for t in range(T + 1):
    dp[0][t] = 0

max_visited = 0
for i in range(1, n + 1):
    for t in range(T + 1):
        if dp[i - 1][t] > max_visited:
            max_visited = dp[i - 1][t]
        if t >= edges[i - 2][2]:
            dp[i][t] = max(dp[i-1][t], dfs(i, t) + 1)
        else:
            dp[i][t] = dp[i-1][t]

k = max_visited
path = []
curr_vertex = n
remaining_time = T
while k > 0:
    path.append(curr_vertex)
    for edge in reversed(edges):
        u, v, time_taken = edge
        if curr_vertex == v and remaining_time >= time_taken:
            curr_vertex = u
            remaining_time -= time_taken
            break
    k -= 1

print(k)
print(' '.join(map(str, path[::-1])))
