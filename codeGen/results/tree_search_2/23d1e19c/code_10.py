from collections import deque

def min_max_recomputation(graph, fixed_path):
    n = len(graph)
    memo = {}
    dp = [[float('inf'), float('-inf')] for _ in range(n)]

    def dfs(v, path):
        if (v, tuple(path)) in memo:
            return memo[(v, tuple(path))]
        
        if v == t:
            return 0, 0
        
        min_rec, max_rec = float('inf'), 0
        for u in graph[v]:
            prev_path = path + [u]
            rec, _ = dfs(u, prev_path)
            dp[u][0] = min(dp[u][0], dp[v][0] + 1 + rec)
            dp[u][1] = max(dp[u][1], dp[v][1] + 1 + rec)
        
        memo[(v, tuple(path))] = (dp[v][0] + 1, dp[v][1] + 1)
        return *memo[(v, tuple(path))]

    t_idx = [i for i, v in enumerate(fixed_path) if v == t][0]
    return dp[t_idx][0], dp[t_idx][1]
