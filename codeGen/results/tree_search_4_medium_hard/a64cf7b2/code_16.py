def dfs(graph, n, T):
    dp = [[0] * (T + 1) for _ in range(n + 1)]
    
    def helper(i, T):
        if i == n:
            return 1
        if dp[i][T] != 0:
            return dp[i][T]
        
        max_visit = 0
        for edge in graph:
            u, v, t = edge
            if u == i and v < n and t <= T:
                max_visit = max(max_visit, helper(v, T - t) + 1)
        dp[i][T] = max_visit
        return max_visit
    
    return helper(0, T)


n, m, T = map(int, input().split())
graph = []
for _ in range(m):
    u, v, t = map(int, input().split())
    graph.append((u - 1, v - 1, t))
print(dfs(graph, n, T))

