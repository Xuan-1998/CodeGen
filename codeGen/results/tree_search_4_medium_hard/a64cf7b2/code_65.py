from collections import defaultdict

def max_vertices(n, m, T):
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))

    dp = [[[0] * (n + 1) for _ in range(T + 1)] for _ in range(n + 1)]
    memo = {(t, i): [0] for t in range(T + 1) for i in range(n + 1)}

    def dfs(t, i):
        if dp[i][t][0]:
            return dp[i][t][0], dp[i][t][1]

        max_vertices, path = 0, []
        for v, time_taken in graph.get(i, []):
            new_t, new_path = dfs(t - time_taken, v)
            if len(new_path) + 1 > max_vertices:
                max_vertices = len(new_path) + 1
                path = [i] + new_path

        dp[i][t][0], dp[i][t][1] = max_vertices, path
        return max_vertices, path

    dfs(T, n)
    print(len(dfs(T, n)[1]))
    print(' '.join(map(str, dfs(T, n)[1])))
