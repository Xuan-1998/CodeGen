import sys
from collections import defaultdict

def read_input():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return n, m, graph

def dp(n, m, graph):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    tail = [0] * (n + 1)
    spine = [0] * (n + 1)

    for i in range(2, n + 1):
        for j in range(m + 1):
            if dp[i - 1][j]:
                dp[i][j] = max(dp[i - 1][j], tail[i - 1])
            else:
                for u, v in graph.items():
                    if len(v) > 0 and (u == i or v[0] == i):
                        for k in v:
                            if k != i:
                                if dp[k - 1][j]:
                                    dp[i][j] = max(dp[i][j], spine[i - 1] + j)
                                    break
                        break

    return dp[n][m]

n, m, graph = read_input()
print(dp(n, m, graph))
