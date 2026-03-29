def main():
    n, m, T = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v, t = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((u, v, t))
    visited = set()
    k = len(dfs(graph, 1, T, visited))
    print(k)
    for vertex in sorted(list(visited)):
        print(vertex)

if __name__ == "__main__":
    main()

code_block_end
