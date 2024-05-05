import sys

def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, edges

def dfs(graph, used_edges, path_length, visited):
    if path_length > len(graph):
        return 0
    max_beauty = 0
    for edge in range(len(used_edges)):
        if not visited[used_edges[edge]]:
            new_path_length = path_length + 1
            new_used_edges = set(used_edges)
            new_used_edges.add(edge)
            beauty = dfs(graph, list(new_used_edges), new_path_length, visited.copy())
            if beauty > max_beauty:
                max_beauty = beauty
    return max_beauty

def solve(n, m, edges):
    graph = [i for i in range(1, n+1)]
    used_edges = set()
    visited = [False] * len(edges)
    for edge in edges:
        u, v = edge[0], edge[1]
        if not visited[graph.index(u)] and not visited[graph.index(v)]:
            graph.insert(graph.index(v), u)
            used_edges.add(used_edges.index(edge))
            visited[edges.index(edge)] = True
    return dfs(list(graph), list(used_edges), 0, visited)

n, m, edges = read_input()
print(solve(n, m, edges))

