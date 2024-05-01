from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
fixed_path = list(map(int, input().split()))
k = fixed_path[0]

dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

for i in range(1, k):
    u, v = map(int, input().split())
    graph[u].append(v)

for i in range(k - 1, -1, -1):
    if fixed_path[i] not in graph:
        dp[fixed_path[i]][0] = 0
    for j in range(0, k + 1):
        if j > 0 and i != k:
            dp[fixed_path[i]][j] = min(dp[fixed_path[i]][j], dp[fixed_path[i - 1]][min(j - 1, 0)] + (1 if fixed_path[i] in graph else 0))
    print(f"{dp[-1][k]} {dp[-1][k - 1]}")
