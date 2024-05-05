def dp(t, path):
    if t == 0 or len(path) == n:  # base case: reached vertex n or time limit exceeded
        return 1 if len(path) == n else 0

    max_vertex_count = 0
    for u, v, edge_weight in edges:
        if u == path[-1]:  # edge from current vertex to its neighbor
            new_path = path + [v]
            max_vertex_count = max(max_vertex_count, dp(t - edge_weight, new_path) + 1)
    return max_vertex_count

n, m, T = map(int, input().split())
edges = [(int(u), int(v), int(edge_weight)) for _ in range(m)]

dp_table = {}
for t in range(T, -1, -1):  # construct dp table row by row
    for path in get_paths(t):
        if (t, tuple(path)) not in dp_table:
            dp_table[(t, tuple(path))] = dp(t, list(path))

optimal_route = []
current_vertex = n
while current_vertex > 1:  # backtracking from vertex n to vertex 1
    max_edge_weight = 0
    for edge_weight in [edge[2] for edge in edges if edge[0] == current_vertex]:
        next_vertex = [edge[1] for edge in edges if edge[0] == current_vertex and edge[2] == edge_weight][0]
        if (T - edge_weight, tuple(list(path) + [next_vertex])) in dp_table:
            max_edge_weight = max(max_edge_weight, edge_weight)
    optimal_route.append(current_vertex)
    current_vertex -= 1
print(len(optimal_route))
print(*optimal_route[::-1], sep='\n')
