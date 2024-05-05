import sys
n, m, T = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    edges.append((t, u, v))
edges.sort()

in_degree = [0] * (n + 1)
for t, u, v in edges:
    in_degree[v] += 1
vertices = []
while True:
    if len(vertices) == n:
        break
    for i in range(n):
        if in_degree[i] == 0:
            vertices.append(i)
            for j in range(n):
                if j != i and in_degree[j] > 0:
                    in_degree[j] -= 1

dp = [0] * (n + 1)
for t, u, v in edges:
    for i in range(n):
        if i == v and t <= T - dp[u]:
            dp[v] = max(dp[v], dp[u] + 1)

k = max(dp)
print(k)
for i in range(1, n):
    if dp[i] == k:
        print(i, end=' ')
