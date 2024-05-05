import sys
from collections import defaultdict

n = int(input())
w = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n-1):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

dp = [[0] * (10**9 + 5) for _ in range(n+1)]

def dfs(city, gas):
    if city == n:
        return gas
    if dp[city][gas]:
        return gas

    for neighbor, length in graph[city]:
        new_gas = min(gas - length, w[neighbor] - length)
        dp[city][new_gas] = 1
        result = dfs(neighbor, new_gas)
        if result > gas:
            gas = result
    return gas

print(max(dfs(i, j) for i in range(n+1) for j in range(w[i]+1)))
