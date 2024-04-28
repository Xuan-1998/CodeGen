def min_max_recomputations(graph, path):
    n = len(graph)
    k = len(path) - 1
    dp = [[0, float('inf')] for _ in range(n)]

    # Initialize DP table with base case
    dp[path[0]][[]] = [0, 0]

    for i in range(1, k + 1):
        v = path[i]
        prev_path = path[:i]
        if v == t:
            break

        min_recomp = float('inf')
        max_recomp = 0
        for w in graph[v]:
            if w not in prev_path:
                dp[w][prev_path + [w]] = [dp[v][prev_path][1] + 1, dp[v][prev_path][1]]
                min_recomp = min(min_recomp, dp[w][prev_path + [w]][0])
                max_recomp = max(max_recomp, dp[w][prev_path + [w]][1])

        dp[v][prev_path + [v]] = [min_recomp, max_recomp]

    return dp[t][[]]
