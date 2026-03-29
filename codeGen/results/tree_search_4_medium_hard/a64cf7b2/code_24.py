import sys

n, m, T = map(int, input().split())

# Initialize the DP table with zeros
dp = [[0] * (T + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = 1

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# Sort the edges by their weights
edges.sort()

max_vertices = 0
visited_vertices = []

for edge in reversed(edges):
    w, u, v = edge
    for t in range(T, -1, -1):
        if dp[u][t] and t >= w:
            dp[v][min(t, T)] += 1
            visited_vertices.append(v)
            break

print(len(visited_vertices), *visited_vertices, sep='\n')
