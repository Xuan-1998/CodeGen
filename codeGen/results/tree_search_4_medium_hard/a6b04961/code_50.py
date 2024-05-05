import sys

# Read input
n, m = map(int, input().split())
edges = [[int(i) for i in line.split()] for line in [line.strip() for line in sys.stdin.readlines()][1:]]

# Sort edges by the first vertex and then by the second vertex
edges.sort()

dp = [[0] * (n + 1) for _ in range(n + 1)]

for t in range(2, n + 1):
    dp[t][t] = 1

for i in range(m):
    u, v = edges[i]
    for t in range(min(u, v), n + 1):
        if dp[t - 1][u]:
            dp[t][v] = max(dp[t][v], dp[t - 1][u])
        if dp[t - 1][v]:
            dp[t][u] = max(dp[t][u], dp[t - 1][v])

# Calculate the maximum beauty
max_beauty = 0
for t in range(2, n + 1):
    for u in range(t, n + 1):
        if dp[t][u]:
            max_beauty = max(max_beauty, (n - t) * (m - sum(dp[i][j] for i in range(t, n + 1) for j in range(i, n + 1) if dp[i][j])))

print(max_beauty)
