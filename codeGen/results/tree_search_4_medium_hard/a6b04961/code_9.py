if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append((v, u))
        graph[v].append((u, v))

    _, spines = dfs(graph, memo)
    print(len(spines) * (n - len(set(map(lambda x: x[0] or x[1], spines))) + 1))
