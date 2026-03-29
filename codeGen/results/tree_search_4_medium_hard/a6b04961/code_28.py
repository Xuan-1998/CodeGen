import sys

def max_hedgehog_beauty():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [0] * (n + 1)
    max_beauty = 0

    for i in range(2, n+1):
        if not graph[i]:
            continue
        dp[i] = max(dp[i-1], min(dp[j] for j in graph[i]) + 1)

    for i in range(n, 1, -1):
        max_beauty = max(max_beauty, dp[i-1] * (n - i + 1))

    print(max_beauty)

max_hedgehog_beauty()
