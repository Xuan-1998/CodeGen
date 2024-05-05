import sys
from collections import defaultdict

def gas_stations():
    n = int(input())
    w = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
        graph[v].append((u, c))

    dp = [[[0] * (10**9 + 1) for _ in range(2)] for _ in range(n)]
    max_gas = [[0] * (10**9 + 1) for _ in range(n)]

    def dfs(i, j):
        if dp[i][j][1]:
            return max_gas[i][j]
        dp[i][j][1] = True
        max_gas[i][j] = j
        for k, c in graph[i]:
            if c <= j:
                max_gas[i][j] = max(max_gas[i][j], dfs(k, j - c))
        return max_gas[i][j]

    print(dfs(0, w[0]))

gas_stations()
