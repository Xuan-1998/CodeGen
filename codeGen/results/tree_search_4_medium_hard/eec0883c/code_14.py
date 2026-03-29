import sys
from collections import defaultdict

def dfs(node, visited, dp, gas):
    if visited[node]:
        return dp[node]
    visited[node] = True
    min_gas = float('inf')
    for neighbor, distance in gas[node].items():
        remaining_gas = max(0, gas[node] - distance) + dfs(neighbor, visited, dp, gas)
        min_gas = min(min_gas, remaining_gas)
    dp[node] = min_gas
    return dp[node]

def solve(n, w, c):
    gas = defaultdict(dict)
    for i in range(1, n):
        u, v, cost = map(int, input().split())
        gas[u][v] = cost
        gas[v][u] = cost  # assuming the graph is undirected
    dp = [0] * (n + 1)
    visited = [False] * (n + 1)
    for i in range(1, n):
        dfs(i, visited, dp, gas)
    return dp[-1]

if __name__ == "__main__":
    n = int(input())
    w = list(map(int, input().split()))
    print(solve(n, w, c))
