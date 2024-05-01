import sys

# Read input
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
fixed_path = list(map(int, input().split()))
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

# Initialize dp array with infinity
dp = [[(sys.maxsize, sys.maxsize) for _ in range(n + 1)] for _ in range(n + 1)]

# Base case: update dp[t][t] to (0, 0)
dp[fixed_path[-1]][fixed_path[-1]] = (0, 0)

# State transition
for i in range(n - 1, -1, -1):
    for j in graph[i]:
        if i == fixed_path[0]: continue  # skip the first vertex of the fixed path
        for p in fixed_path:
            if i < p and p < j:  # edge from u to p and from p to v
                dp[i][j] = min(dp[i][p], (1, 1)) + dp[p][j]

# Return minimum and maximum values in the dp array
min_recomputations = min(min(row) for row in dp)
max_recomputations = max(max(row) for row in dp)

print(min_recomputations, max_recomputations)
