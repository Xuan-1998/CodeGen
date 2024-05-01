import sys

def solve(n, m, edges, k, path):
    dp = [float('inf')] * (n + 1)
    for i in range(k - 1):
        j = path[i]
        for p in range(1, n + 1):
            if is_reachable(j, p) and p not in path[:i]:
                dp[p] = min(dp[p], dp[j] + 1)
    return (dp[0], dp[0])

def is_reachable(u, v):
    for edge in edges:
        if edge[0] == u and edge[1] == v:
            return True
    return False

# Input handling
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
path = list(map(int, input().split()))

print(*solve(n, m, edges, k, path))
