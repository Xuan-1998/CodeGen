import sys

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

s, t, k = map(int, input().split())
fixed_path = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(n + 1):
    if i not in fixed_path:
        max_recomputations = 0
        for v in graph[i]:
            if v in fixed_path:
                continue
            max_recomputations = max(max_recomputations, dp[v] + 1)
        dp[i] = 1 + max_recomputations

min_recomputations, max_recomputations = float('inf'), -float('inf')
for i in range(n + 1):
    min_recomputations = min(min_recomputations, dp[i])
    max_recomputations = max(max_recomputations, dp[i])

print(min_recomputations, max_recomputations)
