code = """
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

k = int(input())
path = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(k + 1)]
max_dp = [[0] * (n + 1) for _ in range(k + 1)]

memoization = {i: {j: 0 for j in range(1, n + 1)} for i in range(k + 1)}

for i in range(2, k + 1):
    for j in range(1, n + 1):
        if (u, v) in edges and u == i:
            dp[i][j] = min((memoization[i - 1].get(k, float('inf')) + 1 for k in range(1, n + 1) if (k, j) in edges and k != j), default=float('inf'))
        else:
            dp[i][j] = dp[i - 1][j]

for i in range(2, k + 1):
    for j in range(1, n + 1):
        max_dp[i][j] = max((memoization[i - 1].get(k, float('inf')) + 1 for k in range(1, n + 1) if (k, j) in edges and k != j), default=0)
        if not (u, v) in edges or u != i:
            max_dp[i][j] = max(max_dp[i - 1][j], memoization[i - 1].get(j, float('inf')))

print(min(max_dp[k][path[-1]], dp[k][path[-1]]), max(max_dp[k][path[-1]], dp[k][path[-1]]))
"""

