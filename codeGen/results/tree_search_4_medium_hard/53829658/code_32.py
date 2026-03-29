from collections import defaultdict

def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [float('inf')] * (n+1)
    parent = [-1] * (n+1)
    for city in range(1, n+1):
        for neighbor in graph[city]:
            if dp[neighbor] + 1 < dp[city]:
                dp[city] = dp[neighbor] + 1
                parent[city] = neighbor

    min_edges_to_invert = max(dp)
    capital_cities = [i for i, edges in enumerate(dp) if edges == min_edges_to_invert]
    print(min_edges_to_invert)
    print(*capital_cities)

solve()
