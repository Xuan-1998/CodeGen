import sys

def solve():
    n, m, T = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    # Sort edges by their weights
    edges.sort(key=lambda x: x[2])

    dp = [[0] * (T + 1) for _ in range(n + 1)]
    memo = {}

    def dfs(i, t):
        if (i, t) in memo:
            return memo[(i, t)]

        max_vertices = 0
        for j, (u, v, weight) in enumerate(edges):
            if u == i and dp[v][t - weight] > dp[i][t]:
                vertices = dfs(v, t - weight) + 1
                if vertices > max_vertices:
                    max_vertices = vertices

        memo[(i, t)] = max_vertices
        return max_vertices

    result = []
    for i in range(n):
        if i > 0 and dp[i][T] > dp[i-1][T]:
            result.append(i)
        else:
            break

    print(len(result))
    print(' '.join(map(str, result)))

solve()
