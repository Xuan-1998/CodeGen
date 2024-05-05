def max_vertices(n, m, T):
    graph = {}
    for _ in range(m):
        u, v, t = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, t))

    memo = {}

    def dfs(i, time):
        if i == n:
            return 1
        if (i, time) in memo:
            return memo[(i, time)]
        visited = 0
        for j, t in graph.get(i, []):
            if t <= time and not dfs(j, time - t):
                continue
            visited += 1
        memo[(i, time)] = visited
        return visited

    return str(dfs(1, T)), '\n'.join(map(str, range(2, n+1)))

if __name__ == '__main__':
    n, m, T = map(int, input().split())
    print(*max_vertices(n, m, T), sep='\n')
