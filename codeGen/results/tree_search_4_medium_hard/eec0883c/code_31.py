import sys

def solve():
    n, *gasoline_capacities = map(int, input().split())
    graph = {}
    for _ in range(n - 1):
        u, v, capacity = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, capacity))
        graph[v].append((u, capacity))

    dp = [c for c in gasoline_capacities]
    for city, edges in graph.items():
        for neighbor, capacity in edges:
            dp[city - 1] = max(dp[city - 1], min(dp[city - 1], capacity) + dp[neighbor - 1])

    print(max(dp))

solve()
