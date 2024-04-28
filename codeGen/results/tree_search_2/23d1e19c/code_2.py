import sys

n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))

dp = [[[0, 0]] for _ in range(n)]

for i in range(k):
    v = path[i]
    dp[v][i] = [1 + dp[path[i-1]][i-1][0], 1 + dp[path[i-1]][i-1][1]]

for i in range(k+1, n):
    for prev_path in graph:
        if all(j not in path[:i] for j in graph[prev_path]):
            min_recomp = sys.maxsize
            max_recomp = 0
            for neighbor in graph[prev_path]:
                if all(j not in path[:i] for j in graph[neighbor]):
                    min_recomp = min(min_recomp, dp[neighbor][i-1][0])
                    max_recomp = max(max_recomp, dp[neighbor][i-1][1])
            dp[prev_path][i] = [min_recomp + 1, max_recomp + 1]

print(min(dp[-1]), max(dp[-1]))
