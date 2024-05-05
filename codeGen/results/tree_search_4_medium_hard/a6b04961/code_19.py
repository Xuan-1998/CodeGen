def solve():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        max_beauty = 0
        for j in range(i):
            if j not in visited:
                new_beauty = dp[j-1] + 1
                if graph.get(j, []).difference(visited):
                    new_beauty += 1
                max_beauty = max(max_beauty, new_beauty)
        dp[i] = max_beauty

    return dp[-1]

print(solve())
