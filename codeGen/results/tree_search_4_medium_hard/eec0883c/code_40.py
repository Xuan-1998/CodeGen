import sys
from collections import defaultdict

def solve():
    n = int(input())
    max_gas_available = [int(x) for x in input().split()]
    roads = []
    for _ in range(n - 1):
        u, v, c = map(int, input().split())
        roads.append((u, v, c))

    dp = [[0] * (max_gas_available[0] + 1) for _ in range(n)]

    for i, road in enumerate(roads):
        u, v, c = road
        for j in range(max_gas_available[i]):
            if j <= max_gas_available[u - 1]:
                dp[v][j] = max(dp[v][j], dp[u][min(j, max_gas_available[u - 1])] + min(c, j))
    return max(dp[-1])

print(solve())
