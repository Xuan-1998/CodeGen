import sys
from collections import defaultdict

def max_gas(n, w, roads):
    # Create graph with n nodes and edges
    g = defaultdict(list)
    for u, v, c in roads:
        g[u].append((v, c))
        g[v].append((u, 0))  # Add reverse edge for buying gas

    # Initialize dynamic programming state
    dp = [0] * (n + 1)

    def dfs(node):
        if dp[node] > 0: return dp[node]
        dp[node] = w[node - 1]  # Buying gas at this city
        for neighbor, capacity in g[node]:
            if capacity > 0:
                dp[node] = max(dp[node], dfs(neighbor) + capacity)
        return dp[node]

    return dfs(1)

# Read input from stdin
n = int(input())
w = list(map(int, input().split()))
roads = []
for _ in range(n - 1):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

print(max_gas(n, w, roads))
