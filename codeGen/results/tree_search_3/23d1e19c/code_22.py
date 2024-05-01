# BEGIN SOLUTION
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))
    max_recomputation = 0

    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(n):
        if i < k:
            dp[i + 1] = min(dp[i], 1) if path[i] == i else float('inf')
        else:
            max_recomputation = max(max_recomputation, dp[i])
            for v in graph[path[i]]:
                if i - v > max_recomputation:
                    dp[v] = min(dp[v], dp[i] + 1)
    return min(dp), max_recomputation

print(*solve(), sep=' ')
