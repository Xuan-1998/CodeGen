def check_components(graph, visited):
    xor_values = set()
    while any(not v in visited for v in graph):
        u = next(v for v in graph if not v in visited)
        visited = dfs(u, visited)
        xor_value = 0
        for node in visited:
            xor_value ^= graph[node]
        xor_values.add(xor_value)
    return len(xor_values) == 1

def is_possible_to_delete_edges(n, k, values, edges):
    graph = {i: value for i, value in enumerate(values)}
    visited = set()
    if check_components(graph, visited):
        return "YES"
    else:
        return "NO"

# Example usage
n, k = map(int, input().split())
values = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n-1)]
print(is_possible_to_delete_edges(n, k, values, edges))
