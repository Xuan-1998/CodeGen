def min_max_recomputation():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))

    dp = [[float('inf'), 0] for _ in range(n)]
    dp[path[0]][path[-1]] = [0, 0]

    for i in range(k - 1):
        u = path[i]
        v = path[i + 1]
        for p in graph[u]:
            if p == v:
                break
            dp[u][v] = min((max(dp[u][p][0], 1) + dp[p][v]), (max(dp[u][p][1], 1) + dp[p][v]))
        else:
            continue
        for w in graph[v]:
            if w != u and w != p:
                dp[v][w] = min((max(dp[v][w][0], 1) + dp[w][t]), (max(dp[v][w][1], 1) + dp[w][t]))

    print(min(dp[s][t]))
    print(max(dp[s][t]))
