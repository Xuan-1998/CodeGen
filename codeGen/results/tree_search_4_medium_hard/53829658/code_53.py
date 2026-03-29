from collections import defaultdict

def solve():
    n = int(input())
    edges = defaultdict(int)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges[u] += 1
        edges[v] += 0  # Not an edge, just a marker for the capital

    max_in_degree = max(edges.values(), default=0)
    capital = [i + 1 for i, x in enumerate(edges) if x == max_in_degree][0]
    print(capital)

    dp = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        for i in range(1, n + 1):
            if i == v:
                continue
            if edges[i]:
                continue
            dp[v] = max(dp[u] + 1, dp[v])
    print(max(dp))

solve()
