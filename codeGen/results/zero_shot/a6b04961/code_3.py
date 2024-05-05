import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    return graph, n

def dfs(graph, node, visited, path):
    if len(path) > 0:
        last_node = path[-1]
        for next_node in graph[last_node]:
            if next_node not in visited:
                visited.add(next_node)
                path.append(next_node)
                dfs(graph, next_node, visited, path)
                path.pop()
                break
    return path

def find_hedgehog(graph):
    n = len(graph)
    visited = set()
    tail = []
    for node in range(1, n+1):
        if node not in visited:
            path = [node]
            visited.add(node)
            path = dfs(graph, node, visited, path)
            if len(path) > 0 and len(tail) == 0 or path[-1] != tail[-1]:
                tail = path
    spine_count = m - sum(1 for u in range(n+1) if graph[u])
    return len(tail) * spine_count

graph, n = read_input()
print(find_hedgehog(graph))
