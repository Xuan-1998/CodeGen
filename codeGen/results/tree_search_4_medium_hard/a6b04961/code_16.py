from collections import defaultdict

def hedgehog_beauty():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(i):
            if any(vertex in graph[j] for vertex in graph[i]):
                dp[i] = max(dp[i], dp[j - 1] + len(graph[i]))
    return dp[-1]
