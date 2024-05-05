### BEGIN CODE
from collections import defaultdict

def read_input():
    n, m, T = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
    return n, graph, T

def solve(n, graph, T):
    dp = [[0] * (T+1) for _ in range(n+1)]
    for i in range(2, n+1):
        for j in range(T+1):
            dp[i][j] = dp[i-1][j]
            for u, w in graph.get(i-1, []):
                if j >= w:
                    dp[i][min(j, j-w)] = max(dp[i][min(j, j-w)], dp[u][max(0, j-w)] + 1)
    return dp[n][T] - 1

n, graph, T = read_input()
print(solve(n, graph, T))
