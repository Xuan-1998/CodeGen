import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, edges

def dfs(graph, path, visited, spine_count):
    if len(path) > 1:
        yield path
    for neighbor in graph[path[-1]]:
        if neighbor not in visited and (neighbor not in path or path.index(neighbor) == 0):
            new_path = list(path)
            new_path.append(neighbor)
            visited.add(neighbor)
            yield from dfs(graph, new_path, visited, spine_count + (neighbor not in [edge[1] for edge in edges if edge[0] in path]))
            visited.remove(neighbor)

def find_max_beauty(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    max_beauty = 0
    for path in dfs(graph, [0], set([0]), 0):
        spine_count = 0
        for edge in edges:
            if edge[1] not in path and edge[0] in path:
                spine_count += 1
        beauty = len(path) * (spine_count + 1)
        max_beauty = max(max_beauty, beauty)

    return max_beauty

if __name__ == "__main__":
    n, edges = read_input()
    print(find_max_beauty(n, edges))
