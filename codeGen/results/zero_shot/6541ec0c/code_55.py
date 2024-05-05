def can_delete_edges():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Group nodes by connected components
    graph = {}
    for edge in edges:
        u, v = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Calculate node values for each connected component
    component_values = {}
    visited = set()
    for node in graph:
        if node not in visited:
            value = 0
            stack = [node]
            while stack:
                current_node = stack.pop()
                if current_node not in visited:
                    visited.add(current_node)
                    value ^= values[current_node-1]
                    stack.extend(neighbor for neighbor in graph[current_node] if neighbor not in visited)
            component_values[node] = value

    # Check if k-1 edges can be removed
    for node, value in component_values.items():
        if len(graph[node]) > 0:
            print("YES" if len(graph[node]) <= k else "NO")

can_delete_edges()
