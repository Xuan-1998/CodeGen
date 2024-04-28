from collections import defaultdict

def min_max_recomputations(n, m, edges, k, path):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    dp = [[[0, 0] for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        if i == path[0]:
            break
        dp[i][i-1] = [0, 0]

    for u in range(k-1, -1, -1):
        for v in graph[path[u]]:
            for p in range(path[u-1], path[u]+1):
                dp[v][p] = min(max(dp[u][v][0], dp[p][u][0]), max(dp[u][v][1], dp[p][u][1]))
                if u == 0:
                    break

    return [min(dp[0][k-1][0], dp[0][k-1][1]), max(dp[0][k-1][0], dp[0][k-1][1])]

n, m = map(int, input().split())
edges = [(i, j) for i in range(1, n+1) for j in range(n) if i != j]
k = int(input())
path = list(map(int, input().split()))
print(*min_max_recomputations(n, m, edges, k, path))
