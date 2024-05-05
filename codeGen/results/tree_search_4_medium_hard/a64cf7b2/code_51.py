def max_vertices(n, m, T):
    edges = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges.append((u, v, t))

    dp = [[0] * (T + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if i == n:
            return 1 if j >= 0 else 0
        if dp[i][j]:
            return dp[i][j]

        max_vertices = 0
        for u, v, t in edges:
            if u < i and t <= j:
                max_vertices = max(max_vertices, dfs(u, j - t) + 1)
        dp[i][j] = max_vertices
        return dp[i][j]

    k = dfs(1, T)
    route = []
    j = T
    for i in range(n):
        max_vertices = 0
        for u, v, t in edges:
            if u < i and t <= j:
                vertices = dfs(u, j - t) + 1
                if vertices > max_vertices:
                    max_vertices = vertices
                    route.append(i)
        j -= 1

    print(k)
    print(*route[::-1], sep='\n')
