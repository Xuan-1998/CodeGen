def min_max_recomputation(graph, path):
    n = len(graph)
    dp = [[(float('inf'), float('-inf')) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = (0, 0)  # base case: no need to recalculate at this point

    for v in range(n - 1):
        u = path[v]
        t = path[v + 1]

        if graph[u][t] == 1:
            dp[u][t] = ((v + 2), (v + 2))  # min and max number of recalculation is the same
        else:
            dp[u][t] = (dp[t][v], dp[t][v])  # no need to recalculate, so both are equal

    for k in range(n - 1):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    min_rec, max_rec = dp[i][k]
                    new_min_rec = (min_rec + 1) if dp[k][j] != ((k + 1), (k + 1)) else min_rec
                    new_max_rec = (max_rec + 1) if dp[k][j] != ((k + 1), (k + 1)) else max_rec

                    dp[i][j] = (min(new_min_rec, max_rec), max(new_min_rec, max_rec))

    return dp[0][-1]
