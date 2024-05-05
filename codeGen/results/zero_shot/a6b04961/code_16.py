def dfs(graph, vertex, visited, path):
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.add(neighbor)
            path.append(neighbor)
            yield from dfs(graph, neighbor, visited, path)
            visited.remove(neighbor)
            path.pop()

def find_simple_paths(graph):
    max_beauty = 0
    for vertex in range(n):
        visited = set()
        path = [vertex]
        yield from dfs(graph, vertex, visited, path)

for path in find_simple_paths(graph):
    tail_length = len(path)
    spines = sum(1 for edge in edges if edge[0] not in path and edge[1] in path) + sum(1 for edge in edges if edge[1] not in path and edge[0] in path)
    beauty = tail_length * spines
    max_beauty = max(max_beauty, beauty)

print(max_beauty)
