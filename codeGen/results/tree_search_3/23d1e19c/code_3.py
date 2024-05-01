import sys

# Read the graph and path information
n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
k = int(input())
path = list(map(int, input().split()))

# Initialize the dp array
dp = [sys.maxsize] * (n + 1)
dp[path[0]] = 0

# Perform dynamic programming
for i in range(1, k):
    for v in graph[path[i]]:
        if v != path[i - 1]:
            continue
        for j in graph[v]:
            dp[j] = min(dp[j], dp[v] + (1 if v != t else 0))

# Print the result
print(min(dp), max(dp))
