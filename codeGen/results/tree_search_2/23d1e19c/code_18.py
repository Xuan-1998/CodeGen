from collections import defaultdict

def min_max_recomputations():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    s, t = map(int, input().split())
    k, *path = map(int, input().split())

    dp = [[float('inf'), float('-inf')] for _ in range(n + 1)]
    dp[s][0] = 0

    for i in range(1, n):
        v, p = path[i - 1], path[:i]
        if i < k:
            dp[v][1] = 0
        else:
            dp[v][1] = min(dp[t][1], max(dp[u][1] + 1 for u in graph[v]))
        dp[v][0] = min(min(dp[u][0] for u in graph[v]) + (i < k), dp[v][1])

    print(min(dp[-1]), max(dp[-1]))

min_max_recomputations()
