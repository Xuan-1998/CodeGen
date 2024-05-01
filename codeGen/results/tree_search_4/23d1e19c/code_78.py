import sys

def solve():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    
    dp = [[[0] * (k + 1) for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if i == path[j - 1]:
                dp[i][j][0] = 0
            else:
                dp[i][j][0] = 1
    
    for d in range(1, k + 1):
        for v in range(1, n + 1):
            if v in graph and path[d - 1] not in graph[v]:
                for u in graph[v]:
                    if u < v:
                        dp[v][d][0] = min(dp[v][d][0], dp[u][d - 1][0] + 1)
    
    print(min(min([min(row) for row in dp[path[-1]]])))
    print(max(max([max(col) for col in [row for row in dp]])))

solve()
