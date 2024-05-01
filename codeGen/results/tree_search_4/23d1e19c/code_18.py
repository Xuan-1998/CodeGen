import sys

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
p = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(k + 1)]
max_dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(1, n + 1):
        if j == p[i]:
            dp[i][j], max_dp[i][j] = 0, 0
        else:
            dp[i][j] = min((dp[i - 1].index(min(edge)) if edge else float('inf')) for edge in edges if edge[0] == j and edge[1] != j)
            max_dp[i][j] = max((max_dp[i - 1].index(max(edge)) if edge else -1) for edge in edges if edge[0] == j and edge[1] != j)

print(min(dp[-1]), max(max_dp[-1]))
