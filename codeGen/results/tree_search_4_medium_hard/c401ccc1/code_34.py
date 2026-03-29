def has_path(graph, u, v):
    memo = {}
    
    def dfs(w):
        if w not in memo:
            memo[w] = (w & u) == 0
            for i in range(len(graph)):
                if graph[i][1] & w and not dfs(i):
                    return False
            if w != v:
                return True
        return memo[w]
    
    return dfs(v)
