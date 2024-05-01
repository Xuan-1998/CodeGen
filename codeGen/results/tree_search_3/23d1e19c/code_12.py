import sys

# Read input from stdin
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
fixed_path = list(map(int, input().split()))

# Initialize dynamic programming table dp
dp = [0] * (k+1)
for i in range(1, k+1):
    if fixed_path[i-1] not in graph[fixed_path[i-2]]:
        dp[i] = min(dp[j-1] + 1 for j in range(i)) if i > 1 else 0
    else:
        dp[i] = dp[i-1]

# Print the minimum and maximum number of recomputations
print(min(dp), max(dp))
