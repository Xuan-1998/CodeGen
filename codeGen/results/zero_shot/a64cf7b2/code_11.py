import sys

def max_vertices(graph, T):
    n = len(graph)
    dp = [0] * n
    vis = [False] * n

    def dfs(i, t):
        if i == n - 1:
            return 1
        if dp[i]:
            return dp[i]
        if t < 0:
            return 0
        res = 0
        for j in graph[i]:
            if not vis[j]:
                res = max(res, dfs(j, t - dp[i-1]))
        dp[i] = res + 1
        return dp[i]

    res = dfs(0, T)
    path = []
    i = n - 1
    while i > 0:
        for j in graph[i]:
            if not vis[j] and dfs(j, T - dp[i-1]) == res - 1:
                path.append(i)
                i = j
                break
    return res, path[::-1]

n, m, T = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

res, path = max_vertices(graph, T)
print(res)
print(*path, sep='\n')
