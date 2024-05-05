import sys
from collections import defaultdict

# Read input data
n = int(input())
w = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n-1):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

# Initialize DP table
dp = [[0]*max(w) for _ in range(n)]
dp[0][w[0]] = w[0]

# Perform DFS traversal
stack = [(0, w[0])]
while stack:
    node, gas = stack.pop()
    for neighbor, road_length in graph[node]:
        new_gas = min(dp[neighbor-1][gas-road_length], dp[neighbor-1][max(0, gas-road_length)])
        if new_gas > dp[neighbor][new_gas]:
            dp[neighbor][new_gas] = new_gas
            stack.append((neighbor, new_gas))
    if node < n-1:
        dp[node+1][w[node]] = w[node]

# Print the maximum amount of gasoline that Nut can have at the end of the path.
print(max(dp[-1]))

