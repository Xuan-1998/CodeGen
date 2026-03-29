from collections import defaultdict

def max_vertices(n, m, T):
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))

    dp = [[0] * (T + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if dp[i][j]:
            return dp[i][j]
        
        dp[i][j] = 1
        for neighbor, time in graph.get(i, []):
            if time <= j:
                dp[i][j] = max(dp[i][j], dfs(neighbor, j - time) + 1)
        
        return dp[i][j]

    return dfs(n, T)

n, m, T = map(int, input().split())
print(max_vertices(n, m, T))
