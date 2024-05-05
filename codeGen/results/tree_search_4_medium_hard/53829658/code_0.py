import sys

# Read input and initialize variables
n = int(input())
dp = [float('inf')] * (n + 1)
parent = [-1] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    parent[v] = u

# Perform DFS/BFS from the capital and update state expression dp[i]
dp[1] = 0
for i in range(2, n + 1):
    for j in range(i):
        if parent[j] == -1:
            continue
        if dp[j] + 1 < dp[i]:
            dp[i] = dp[j] + 1

# Calculate the minimum number of edges to be reversed
res = float('inf')
for i in range(2, n + 1):
    res = min(res, dp[i] + (n - i))

print(res)
print(*range(1, n + 1), sep=' ')
