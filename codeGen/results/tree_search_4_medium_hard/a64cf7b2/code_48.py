import sys

def max_vertices(graph, T):
    memo = {}
    dp = [[0] * (T + 1) for _ in range(len(graph) + 1)]

    def dfs(u, t):
        if (u, t) in memo:
            return memo[(u, t)]
        k = 0
        for v, w in graph[u]:
            k = max(k, dfs(v, t - w) + 1)
        memo[(u, t)] = k
        return k

    for i in range(1, len(graph) + 1):
        dp[i][T] = dfs(i - 1, T)

    k = dp[-1][-1]
    path = []
    u = len(graph)
    t = T
    while k > 0:
        for v, w in graph[u]:
            if dfs(v, t - w) + 1 == k:
                path.append(u)
                k -= 1
                break
        u -= 1
        t -= 1

    print(k)
    print(' '.join(map(str, path[::-1])))

n, m, T = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

max_vertices(graph, T)
