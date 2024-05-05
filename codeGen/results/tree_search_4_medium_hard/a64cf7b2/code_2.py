from functools import lru_cache

def solve():
    n, m, T = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dp = [[0] * (T + 1) for _ in range(n+1)]

    @lru_cache(None)
    def dfs(i, j):
        if i > n or j < 0:
            return 0
        if dp[i][j] != 0:
            return dp[i][j]
        
        res = 0
        for u, v, t in graph[i]:
            if t <= j:
                res = max(res, dfs(v, j-t) + 1)
            else:
                res = max(res, dfs(u, j))
        dp[i][j] = res
        return res

    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, u, t))

    k = dfs(1, T)
    route = [n]
    j = T - (T - k)

    while True:
        for i, (u, v, t) in enumerate(graph[route[-1]]):
            if t <= j and dp[v][j-t] > 0:
                route.append(v)
                j -= t
                break
        else:
            route.pop()
            if route[-1] == 1:
                break

    print(k)
    print(*route[::-1], sep='\n')

solve()
