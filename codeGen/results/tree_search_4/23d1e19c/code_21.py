from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))
t = path[-1]

dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 0
    for j in graph[i]:
        if i != j:
            for k in range(1, n + 1):
                if edge_exists(i, k) and k != t:
                    dp[k][t] = min(dp[k][t], dp[i][j] + 1)
            for k in range(1, n + 1):
                if edge_exists(j, k) and k != t:
                    dp[k][t] = min(dp[k][t], dp[j][k] + 1)

min_recomputation_times = float('inf')
max_recomputation_times = float('-inf')

for i in range(k - 1, -1, -1):
    for j in range(path[i + 1] + 1, n + 1):
        min_recomputation_times = min(min_recomputation_times, dp[i][j])
        max_recomputation_times = max(max_recomputation_times, dp[i][j])

print(min_recomputation_times, max_recomputation_times)

def edge_exists(u, v):
    for edge in graph[u]:
        if edge == v:
            return True
    return False
