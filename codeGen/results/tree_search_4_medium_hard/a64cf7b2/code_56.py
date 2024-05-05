from collections import defaultdict

def max_visit(edges, T):
    graph = defaultdict(list)
    dp = [[0] * (len(graph) + 1) for _ in range(len(graph) + 1)]

    for u, v, t in edges:
        graph[u].append((v, t))

    def dfs(i, prev):
        if i == len(graph):
            return 1
        if dp[i][prev] > 0:
            return dp[i][prev]

        max_visit = 0
        for j, (t, _) in enumerate(graph[i]):
            if t < T and t + 1 > max_visit:
                max_visit = t + 1
                prev_max_visit = dfs(j, i)
                dp[i][prev] = max(dp[i][prev], prev_max_visit)

        return dp[i][prev]

    return dfs(0, -1), [i for i in range(len(graph)) if dp[i][-1] > 0]


n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

k, route = max_visit(edges, T)
print(k)
print(*route, sep='\n')
