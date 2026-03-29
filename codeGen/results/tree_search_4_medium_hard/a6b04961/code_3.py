from collections import defaultdict

def max_hedgehog_beaauty(n, m, edges):
    # Create a graph represented as an adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    memo = {(i, prev_vertex): 0 for i in range(n+1) for prev_vertex in range(n)}

    max_beauty = 0

    def dfs(i, prev_vertex):
        nonlocal max_beauty
        if i > len(str(max_beauty)):
            return 0
        if (i, prev_vertex) in memo:
            return memo[(i, prev_vertex)]

        beauty = 1 if i == 1 else 0
        for neighbor in graph[prev_vertex]:
            if neighbor < prev_vertex:
                beauty = max(beauty, 1 + dfs(i+1, neighbor))
        memo[(i, prev_vertex)] = beauty
        return beauty

    for vertex in range(n):
        max_beauty = max(max_beauty, dfs(1, vertex))

    return max_beauty


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    print(max_hedgehog_beaauty(n, m, edges))
