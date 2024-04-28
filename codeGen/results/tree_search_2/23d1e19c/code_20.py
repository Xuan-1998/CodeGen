def min_max_recomputations():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

    s, t = map(int, input().split())
    path_length = 0
    prev_v = None
    for p in reversed(map(int, input().split())):
        path_length += 1
        if p not in graph or len(graph[p]) == 0:
            break
        prev_v = p

    dp = [[(float('inf'), float('-inf'))] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][i] = (0, 0)

    for k in range(path_length - 1, -1, -1):
        v, prev_v = t, path[k]
        if prev_v not in graph or len(graph[prev_v]) == 0:
            break
        min_rec, max_rec = float('inf'), float('-inf')
        for j in range(n + 1):
            if j != prev_v and (j, tuple(path[:k])) not in [(i, path) for i, path in enumerate(graph, start=1)]:
                continue
            if k > 0:
                dp[v][prev_v] = min(max(dp[v][j][0], dp[j][prev_v][0] + 1), max(dp[v][j][1], dp[j][prev_v][1] + 1))
            else:
                min_rec, max_rec = min(min_rec, dp[v][j][0]), min(max_rec, dp[v][j][1])
        print(min_rec, max_rec)

min_max_recomputations()
