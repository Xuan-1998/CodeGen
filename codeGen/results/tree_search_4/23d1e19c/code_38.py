from collections import defaultdict

def shortest_recomputation(n, m, edges, k, path):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i == k or i in path:
            dp[i][0] = 1
        else:
            dp[i][0] = float('inf')

    def dfs(i, j):
        if dp[i][j] != float('inf'):
            return dp[i][j]
        if i not in graph:
            return 1
        for u in graph[i]:
            if u < i and u in path:
                dp[i][j] = min(dp[i][j], dfs(u, j) + 1)
            elif u > i and u in path:
                dp[i][j] = max(dp[i][j], dfs(u, j - 1) + 1)
        return dp[i][j]

    res_min = float('inf')
    res_max = 0
    for i in range(n):
        res_min = min(res_min, dfs(i, k))
        res_max = max(res_max, dfs(i, k))
    return str(min(res_min, res_max)) + ' ' + str(max(res_min, res_max))

# Input and Output
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
path = list(map(int, input().split()))
print(shortest_recomputation(n, m, edges, k, path))
